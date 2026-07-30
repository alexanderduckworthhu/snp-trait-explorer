# Methods (Behind the numbers)

How SNP Trait Explorer builds its educational numbers. This page is the
long-form companion to the in-app **Behind the numbers** view.

## Scope

- **Chromosome 22 only** for the tutorial VCF and the curated trait layer.
- **15 non-medical SNP–trait pairs** from the GWAS Catalog (large-N discovery
  studies). No disease-risk markers.
- **Optional PostgreSQL** for ingest and SQL practice; the Streamlit app also
  runs in demo mode from bundled panel counts and curated CSVs.

## Trait scoring

1. Parse a user genotype file (23andMe-like `.txt` or `rsid,genotype` CSV).
2. Match rsIDs against the curated association table.
3. Convert genotypes to integer **dosage** (0 / 1 / 2 copies of the effect
   allele).
4. Score = `dosage × effect_direction`, where direction is `{+1, −1, 0}` from
   the curated table (higher / lower / neutral measurement association).

Scores are transparent rules, not machine-learned trait models. Cards stay
neutral grey on purpose: correlations, not good/bad labels.

## Ancestry sketch

A Random Forest (`n_estimators=100`) maps the same 15 dosages to 1000 Genomes
**super-population** labels (AFR, AMR, EAS, EUR, SAS). Feature importances and
a simple contribution view explain which markers nudged the guess.

This is illustrative only. Consumer ancestry products use hundreds of thousands
of markers; fifteen chr22 SNPs cannot recover fine-scale ancestry.

## Demo vs live database

| Mode | What you see |
|------|----------------|
| Demo (no `DATABASE_URL`) | Public panel totals, curated MAFs, committed `models/ancestry_clf.joblib` |
| Postgres ingest | Real chr22 allele frequencies and SQL analytics from `sql/analysis/` |

The Cloud demo never trains at runtime; models and feature names are committed.

## Sources

- [1000 Genomes Project phase 3](https://www.internationalgenome.org/) (chr22 VCF + sample panel via EBI FTP)
- [GWAS Catalog](https://www.ebi.ac.uk/gwas/) (curated non-medical associations)
- Bundled `data/sample/demo_genotypes.*` for UI demos without a personal kit export

## Limits

- Educational research demo, **not** a medical device or genetic test.
- Uploaded genotypes stay in the Streamlit session only.
- National / continental research labels are study constructs, not modern
  nationality claims.
- Classic consumer traits (earwax, bitter taste, eye color) sit on other
  chromosomes; this demo stays on chr22 so the VCF and trait layer share one
  chromosome.

See also [`CONCEPTS.md`](CONCEPTS.md) for SNP, dosage, MAF, and association wording.
