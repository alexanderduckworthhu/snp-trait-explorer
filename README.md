# SNP Trait Explorer

An educational SQL + light-ML platform that turns raw SNP genotype files into
plain-English, non-medical trait notes for data science candidates targeting
Geneva and Basel digital-health roles.

| | |
|---|---|
| **Status** | Educational research demo. Not a medical device or genetic test. |
| **Data** | 1000 Genomes Project phase 3 (chr22) + GWAS Catalog associations |
| **Stack** | PostgreSQL 15 · Python · scikit-learn · Streamlit |
| **UI languages** | EN / FR / DE / IT / PT / ES / AR / ZH / RU (`src/i18n.py`, sidebar switcher) |

Biology primer: [`docs/CONCEPTS.md`](docs/CONCEPTS.md)

---

## Why it exists

Consumer genomics kits export raw SNP lists that most people cannot interpret,
while public catalogs already document large-N associations for benign traits.
This project builds the layer between those files and an honest educational
report: curated non-medical associations, transparent dosage scoring, and
population context from 1000 Genomes, without disease-risk claims.

Classic consumer examples such as earwax (`rs17822931`, chr16) or bitter taste
(`TAS2R38`, chr12) are not on chromosome 22. The 15 curated associations here
are real large-N GWAS Catalog hits that *are* on chr22, so the tutorial VCF and
the trait layer share one chromosome.

---

## Technical decisions

- **PostgreSQL 15 for variants / samples / genotypes / associations**,
  considered Pandas-only notebooks and DuckDB; chose Postgres because the
  interview skill target is intermediate SQL (CTEs, windows, `corr()`) and
  normalised reference tables match how health-data teams keep audit-friendly
  stores. DuckDB remains the scale-up path for full-genome VCF without a server.
- **Random Forest (`n_estimators=100`) for super-population labels**,
  considered multinomial logistic regression; forests handle non-linear
  allele-frequency interactions, expose native feature importance, and pair
  with `shap.TreeExplainer` for per-sample explanations.
- **Integer dosage (0/1/2 alternate copies) instead of one-hot genotypes**,
  considered string genotypes in SQL; dosage preserves allele-count order,
  keeps the feature matrix compact, and matches GWAS scoring conventions.
- **15 curated chr22 SNPs for the trait and ancestry layers**, considered
  full-chr22 (~50k) features; each association must be explainable in one
  sentence, sourced, and non-medical. `ingest.py --mode full` still loads all
  biallelic chr22 SNPs for SQL practice.
- **Rule-based trait scores (`dosage × {+1,−1,0}`) instead of ML trait
  models**, considered per-trait regressors; a transparent rule is auditable
  in one sentence and avoids invented confidence from 15 markers.
- **EN/FR/DE/IT/ZH/PT/RU UI strings in `src/i18n.py`**, same sidebar language
  pattern as ICU Mortality and Where Needs Overlap, so French localization for
  Geneva interviews is already wired.

---

## Results and metrics

*(Replace placeholders after real 1000 Genomes ingest +
`ml/train_ancestry_classifier.py`.)*

- Panel size (phase 3): **2,504** samples across **5** super-populations
  (AFR 661, AMR 347, EAS 504, EUR 503, SAS 489)
- Curated trait layer: **15** non-medical chr22 SNP–trait pairs from GWAS
  Catalog studies with discovery **N > 10,000**
- Committed demo ancestry classifier (synthetic dosages for Streamlit Cloud):
  **99.6%** test accuracy on a held-out 20% split (n=500); replace with real
  1000G metrics after ingest
- Real 1000G ancestry accuracy target after training: **>90%** on stratified
  hold-out (allele-frequency structure separates continental labels)

Artifacts committed for deploy (never train at runtime):

- `models/ancestry_clf.joblib`
- `models/feature_names.json`
- `outputs/feature_importances.csv`

---

## Data

| Source | What we use | License / access | Notes |
|--------|-------------|------------------|-------|
| 1000 Genomes Project phase 3 | Chr22 multi-sample VCF + sample panel | Public research release (EBI FTP) | Anonymised research genotypes; not clinical samples |
| GWAS Catalog | Curated non-medical SNP–trait pairs on chr22 | EMBL-EBI public catalog | Associations are correlational; effect directions encode higher/lower trait *measurement*, not disease risk |
| Bundled demo genotypes | `data/sample/demo_genotypes.txt` | Project sample | Synthetic educational file for UI demos without a personal kit export |

**Production would need:** explicit consent flows for user-uploaded genotypes,
retention limits, encryption at rest, and removal of any residual disease-linked
markers. This portfolio demo never stores uploaded files beyond the Streamlit
session.

---

## Setup and usage

### Prerequisites

- Python 3.10+
- PostgreSQL 15+ (optional; app runs in demo mode without it)
- ~250 MB disk for the chr22 VCF

```bash
cd snp-trait-explorer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# pip install -r requirements-ingest.txt   # only when ingesting the VCF
cp .env.example .env
```

### Download 1000 Genomes chr22 + panel

Confirmed EBI sizes: VCF **~196 MB** (205,612,353 bytes), panel **~54 KB**.

```bash
bash scripts/download_data.sh
```

### Database schema and ingest (optional)

```bash
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/snp_trait_explorer
bash scripts/init_db.sh
python ingest.py --mode trait
psql "$DATABASE_URL" -f sql/seed_trait_associations.sql
```

### SQL analytics

```bash
psql "$DATABASE_URL" -f sql/analysis/01_population_allele_frequencies.sql
psql "$DATABASE_URL" -f sql/analysis/02_genotype_distribution.sql
psql "$DATABASE_URL" -f sql/analysis/03_trait_association_summary.sql
psql "$DATABASE_URL" -f sql/analysis/05_population_similarity.sql
```

### Train / explain

```bash
python ml/train_ancestry_classifier.py   # real metrics from Postgres
python ml/explain_model.py
python ml/trait_score.py --sample-id HG00096
# or regenerate the committed demo model:
python ml/train_demo_model.py
```

### Dashboard

```bash
streamlit run app.py
```

Language lives at the top of the sidebar (EN/FR/DE/IT/ZH/PT/RU). Upload once
via **Try the sample file** or your own 23andMe/CSV export; Trait profile and
Ancestry share that session file.

---

## What I'd improve next

1. Expand beyond chr22 with **DuckDB** in-process VCF queries so full-genome
   allele frequencies do not require a long-lived Postgres server.
2. Add **PharmGKB** drug-metabolism SNPs (still non-diagnostic) for more
   actionable educational traits than appearance associations alone.
3. Replace the hard Random Forest label with **ADMIXTURE-style soft
   proportions** so mixed ancestry reads as a mixture, not a single box.

---

## Repository map

```text
docs/CONCEPTS.md
data/curated/trait_associations.csv
sql/schema.sql · sql/seed_trait_associations.sql · sql/analysis/
ingest.py
ml/
models/ · outputs/
app.py · constants.py
src/i18n.py · src/styles.py · src/charts.py · src/genotype_session.py
scripts/download_data.sh · scripts/init_db.sh
.streamlit/config.toml
```
