"""
ingest.py — load 1000 Genomes chr22 VCF + sample panel into PostgreSQL.

Biological refresher (see also docs/CONCEPTS.md):
- SNP: a common single-letter DNA difference between people.
- Allele: one possible letter at a SNP (e.g. A or G).
- Genotype: the pair of alleles a person carries (one from each parent).
- rsID: public catalogue name for a SNP (always starts with "rs").
- MAF: Minor Allele Frequency — how common the rarer allele is (0 to 0.5).
- Population / super-population: research ancestry labels (AFR, AMR, EAS, EUR, SAS).
- VCF: Variant Call Format — standard text/binary-friendly format for genomic variants.

Parser choice: cyvcf2 (not PyVCF).
cyvcf2 wraps htslib in C and streams multi-sample VCFs far faster than pure-Python
PyVCF, which matters when chromosome 22 still has ~50k variants × ~2,500 samples.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Iterable, Optional, Sequence, Set

import psycopg2
from psycopg2.extras import execute_values
from tqdm import tqdm

# Dosage encoding: count of alternate-allele copies at a SNP.
#   genotype 0|0 or 0/0 → dosage 0  (no alternate copies)
#   genotype 0|1 or 1|0 → dosage 1  (one alternate copy — heterozygous)
#   genotype 1|1         → dosage 2  (two alternate copies)
# Integers beat string genotypes (e.g. "A/G") for ML because models expect numeric
# feature matrices, dosage preserves allele-count order (0 < 1 < 2), and it is
# compact to store and join in SQL.


DEFAULT_VCF = Path("data/raw/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz")
DEFAULT_PANEL = Path("data/raw/integrated_call_samples_v3.20130502.ALL.panel")

TRAIT_RSIDS = {
    "rs4253754",
    "rs9616409",
    "rs2294239",
    "rs5998619",
    "rs2283847",
    "rs2845466",
    "rs9608828",
    "rs6519133",
    "rs80584",
    "rs2294915",
    "rs2074735",
    "rs3761422",
    "rs5766576",
    "rs28360615",
    "rs2904552",
}


def get_database_url() -> str:
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise SystemExit(
            "DATABASE_URL is not set. Example:\n"
            "  export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/snp_trait_explorer"
        )
    return url


def genotype_to_dosage(gt) -> Optional[int]:
    """Convert a cyvcf2 genotype list [a0, a1, ...] to alternate-allele dosage 0/1/2."""
    if gt is None or len(gt) < 2:
        return None
    a0, a1 = gt[0], gt[1]
    # cyvcf2 uses -1 for missing
    if a0 < 0 or a1 < 0:
        return None
    return int(a0 + a1)


def parse_maf_from_info(variant) -> Optional[float]:
    """
    Prefer AF (allele frequency of ALT) from VCF INFO; MAF = min(AF, 1-AF).
    Falls back to computing from genotypes if AF is absent.
    """
    af = variant.INFO.get("AF")
    if af is None:
        return None
    # AF may be a tuple for multi-allelic sites; we only ingest biallelic SNPs
    if isinstance(af, (list, tuple)):
        af = af[0]
    try:
        af_f = float(af)
    except (TypeError, ValueError):
        return None
    return round(min(af_f, 1.0 - af_f), 4)


def load_panel(panel_path: Path) -> list[tuple]:
    rows = []
    with panel_path.open() as fh:
        header = fh.readline()
        if not header.lower().startswith("sample"):
            raise ValueError(f"Unexpected panel header: {header!r}")
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            sample_id, pop, super_pop, gender = parts[0], parts[1], parts[2], parts[3]
            rows.append((sample_id, pop, super_pop, gender))
    return rows


def batch_insert(cur, sql: str, rows: Sequence[tuple], page_size: int = 5000) -> None:
    if not rows:
        return
    execute_values(cur, sql, rows, page_size=page_size)


def ingest(
    vcf_path: Path,
    panel_path: Path,
    mode: str = "trait",
    max_variants: Optional[int] = None,
) -> None:
    try:
        from cyvcf2 import VCF
    except ImportError as exc:
        raise SystemExit(
            "cyvcf2 is required. Install with: pip install cyvcf2\n"
            f"Original error: {exc}"
        ) from exc

    if not vcf_path.exists():
        raise SystemExit(f"VCF not found: {vcf_path}\nRun: bash scripts/download_data.sh")
    if not panel_path.exists():
        raise SystemExit(f"Panel not found: {panel_path}\nRun: bash scripts/download_data.sh")

    rsid_filter: Optional[Set[str]] = TRAIT_RSIDS if mode == "trait" else None

    conn = psycopg2.connect(get_database_url())
    conn.autocommit = False
    cur = conn.cursor()

    print("Loading sample panel...")
    panel_rows = load_panel(panel_path)
    batch_insert(
        cur,
        """
        INSERT INTO samples (sample_id, population_code, super_population, gender)
        VALUES %s
        ON CONFLICT (sample_id) DO UPDATE SET
            population_code = EXCLUDED.population_code,
            super_population = EXCLUDED.super_population,
            gender = EXCLUDED.gender
        """,
        panel_rows,
    )
    print(f"  samples upserted: {len(panel_rows)}")

    vcf = VCF(str(vcf_path))
    sample_names = list(vcf.samples)
    # Map VCF column order → sample_id (must match panel)
    panel_ids = {r[0] for r in panel_rows}
    missing = [s for s in sample_names if s not in panel_ids]
    if missing:
        print(f"  warning: {len(missing)} VCF samples not in panel (genotypes skipped for those)")

    variant_buf: list[tuple] = []
    genotype_buf: list[tuple] = []
    n_variants = 0
    n_genotypes = 0

    # Approximate progress: chr22 phase3 has ~1.1M sites including indels;
    # biallelic SNPs with rsIDs are a smaller subset (~50k common teaching figure).
    iterator = tqdm(vcf, desc="Parsing VCF", unit="site")

    for variant in iterator:
        # Keep simple biallelic SNPs only (single-letter alleles).
        if not variant.is_snp:
            continue
        if len(variant.ALT) != 1:
            continue
        ref = variant.REF
        alt = variant.ALT[0]
        if ref is None or alt is None or len(ref) != 1 or len(alt) != 1:
            continue

        # rsID may be "." or a semicolon-separated list; take the first rs* token.
        raw_id = variant.ID or ""
        rsid = None
        for token in raw_id.split(";"):
            if token.startswith("rs"):
                rsid = token
                break
        if rsid is None:
            continue
        if rsid_filter is not None and rsid not in rsid_filter:
            continue

        chrom_s = str(variant.CHROM).replace("chr", "")
        try:
            chrom = int(chrom_s)
        except ValueError:
            continue

        maf = parse_maf_from_info(variant)
        variant_buf.append((rsid, chrom, int(variant.POS), ref, alt, maf, None, None))

        # Genotypes: cyvcf2 returns ndarray shape (n_samples, 3+) with alleles in cols 0,1
        gts = variant.genotypes  # list-like of [a0, a1, phased_bool]
        for sample_id, gt in zip(sample_names, gts):
            if sample_id not in panel_ids:
                continue
            dosage = genotype_to_dosage(gt)
            if dosage is None:
                continue
            genotype_buf.append((sample_id, rsid, dosage))

        n_variants += 1
        if len(variant_buf) >= 1000:
            batch_insert(
                cur,
                """
                INSERT INTO variants (rsid, chromosome, position, ref_allele, alt_allele, maf, gene_symbol, trait_category)
                VALUES %s
                ON CONFLICT (rsid) DO UPDATE SET
                    chromosome = EXCLUDED.chromosome,
                    position = EXCLUDED.position,
                    ref_allele = EXCLUDED.ref_allele,
                    alt_allele = EXCLUDED.alt_allele,
                    maf = COALESCE(EXCLUDED.maf, variants.maf)
                """,
                variant_buf,
            )
            variant_buf.clear()

        if len(genotype_buf) >= 20000:
            batch_insert(
                cur,
                """
                INSERT INTO genotypes (sample_id, rsid, dosage)
                VALUES %s
                ON CONFLICT (sample_id, rsid) DO UPDATE SET dosage = EXCLUDED.dosage
                """,
                genotype_buf,
            )
            n_genotypes += len(genotype_buf)
            genotype_buf.clear()
            conn.commit()

        if max_variants is not None and n_variants >= max_variants:
            break
        if rsid_filter is not None and n_variants >= len(rsid_filter):
            # In trait mode we can stop early once all whitelist SNPs are found,
            # but VCF is position-sorted not by rsID — keep scanning.
            pass

    if variant_buf:
        batch_insert(
            cur,
            """
            INSERT INTO variants (rsid, chromosome, position, ref_allele, alt_allele, maf, gene_symbol, trait_category)
            VALUES %s
            ON CONFLICT (rsid) DO UPDATE SET
                chromosome = EXCLUDED.chromosome,
                position = EXCLUDED.position,
                ref_allele = EXCLUDED.ref_allele,
                alt_allele = EXCLUDED.alt_allele,
                maf = COALESCE(EXCLUDED.maf, variants.maf)
            """,
            variant_buf,
        )
    if genotype_buf:
        batch_insert(
            cur,
            """
            INSERT INTO genotypes (sample_id, rsid, dosage)
            VALUES %s
            ON CONFLICT (sample_id, rsid) DO UPDATE SET dosage = EXCLUDED.dosage
            """,
            genotype_buf,
        )
        n_genotypes += len(genotype_buf)

    conn.commit()
    cur.close()
    conn.close()
    vcf.close()

    print(f"Done. variants touched: {n_variants}, genotype rows written (last flush counted): {n_genotypes}")
    print("Next: psql \"$DATABASE_URL\" -f sql/seed_trait_associations.sql")


def main(argv: Optional[Iterable[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Ingest 1000 Genomes chr22 into PostgreSQL")
    parser.add_argument("--vcf", type=Path, default=DEFAULT_VCF)
    parser.add_argument("--panel", type=Path, default=DEFAULT_PANEL)
    parser.add_argument(
        "--mode",
        choices=("trait", "full"),
        default="trait",
        help="trait=only the 15 curated SNPs (fast, powers the app); full=all biallelic chr22 SNPs with rsIDs",
    )
    parser.add_argument("--max-variants", type=int, default=None, help="Debug cap on variants ingested")
    args = parser.parse_args(list(argv) if argv is not None else None)
    ingest(args.vcf, args.panel, mode=args.mode, max_variants=args.max_variants)


if __name__ == "__main__":
    main()
