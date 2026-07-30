"""
Parse uploaded genotype files into effect-allele dosages for trait SNPs.

Genotype string (e.g. AG) = the two DNA letters someone carries at a SNP.
Dosage vs effect allele = how many copies of the research effect letter
are present (0, 1, or 2).
"""

from __future__ import annotations

import re
from io import StringIO

import pandas as pd


def genotype_string_to_effect_dosage(genotype: str, effect_allele: str) -> int | None:
    """Map AA/AG/GG-style calls to copies of effect_allele (0, 1, or 2)."""
    if genotype is None:
        return None
    cleaned = str(genotype).strip().upper().replace("|", "").replace("/", "").replace(" ", "")
    if cleaned in {"--", "NN", "00", "", "NAN"}:
        return None
    if len(cleaned) != 2 or not cleaned.isalpha():
        return None
    effect = effect_allele.upper()
    return int(cleaned[0] == effect) + int(cleaned[1] == effect)


def parse_23andme(text: str) -> pd.DataFrame:
    """Parse 23andMe-like text into a DataFrame with columns rsid, genotype."""
    rows: list[dict[str, str]] = []
    for line in text.splitlines():
        if not line or line.startswith("#"):
            continue
        parts = re.split(r"\s+", line.strip())
        if len(parts) < 4:
            continue
        rsid, _chromosome, _position, genotype = parts[0], parts[1], parts[2], parts[3]
        if not rsid.startswith("rs"):
            continue
        rows.append({"rsid": rsid, "genotype": genotype})
    return pd.DataFrame(rows)


def parse_simple_csv(text: str) -> pd.DataFrame:
    """Parse a CSV with rsid and genotype columns into a two-column DataFrame."""
    frame = pd.read_csv(StringIO(text))
    columns = {column.lower().strip(): column for column in frame.columns}
    if "rsid" not in columns or "genotype" not in columns:
        raise ValueError("CSV must include columns: rsid, genotype")
    renamed = frame.rename(
        columns={columns["rsid"]: "rsid", columns["genotype"]: "genotype"}
    )
    return renamed[["rsid", "genotype"]]


def parse_upload(filename: str, raw_bytes: bytes) -> pd.DataFrame:
    """Parse an uploaded .txt or .csv genotype file into rsid/genotype rows."""
    text = raw_bytes.decode("utf-8", errors="replace")
    if filename.lower().endswith(".csv"):
        return parse_simple_csv(text)
    return parse_23andme(text)


def dosages_against_associations(
    genotypes: pd.DataFrame,
    associations: pd.DataFrame,
) -> dict[str, int]:
    """Return {rsid: dosage} counting copies of each trait effect allele."""
    genotype_by_rsid = dict(zip(genotypes["rsid"], genotypes["genotype"]))
    dosages: dict[str, int] = {}
    for _, row in associations.iterrows():
        rsid = row["rsid"]
        effect_allele = row["effect_allele"]
        if rsid not in genotype_by_rsid:
            dosages[rsid] = 0
            continue
        dosage = genotype_string_to_effect_dosage(genotype_by_rsid[rsid], effect_allele)
        dosages[rsid] = 0 if dosage is None else dosage
    return dosages
