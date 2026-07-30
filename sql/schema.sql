-- SNP Trait Explorer — PostgreSQL 15+ schema
-- See docs/CONCEPTS.md for plain-English biology definitions.

-- SNP = a common single-letter DNA difference between people.
CREATE TABLE IF NOT EXISTS variants (
    rsid            VARCHAR PRIMARY KEY,          -- rsID: public catalogue name for a SNP (e.g. rs429358)
    chromosome      SMALLINT NOT NULL,
    position        BIGINT NOT NULL,              -- locus: genomic address of this SNP on the chromosome
    ref_allele      CHAR(1) NOT NULL,             -- allele: reference (common catalogue) letter at this locus
    alt_allele      CHAR(1) NOT NULL,             -- allele: alternate letter observed in the VCF
    maf             NUMERIC(6, 4),                -- MAF = Minor Allele Frequency: how common the rarer
                                                  -- version of this SNP is in the global sample (0.0 to 0.5)
    gene_symbol     VARCHAR,                      -- nearest gene name; populated for curated trait SNPs
    trait_category  VARCHAR                       -- high-level trait bucket; populated later from associations
);

-- Population: research ancestry/geography label used in genetic studies.
CREATE TABLE IF NOT EXISTS samples (
    sample_id         VARCHAR PRIMARY KEY,
    population_code   VARCHAR(3) NOT NULL,        -- fine-grained population (e.g. GBR, JPT, YRI)
    super_population  VARCHAR(3) NOT NULL,        -- Super-populations: AFR, AMR, EAS, EUR, SAS
    gender            VARCHAR(6) NOT NULL
);

-- Genotype: the pair of alleles a person carries at a SNP.
-- We store dosage = number of alternate-allele copies (0, 1, or 2) instead of strings.
CREATE TABLE IF NOT EXISTS genotypes (
    sample_id VARCHAR NOT NULL REFERENCES samples (sample_id),
    rsid      VARCHAR NOT NULL REFERENCES variants (rsid),
    dosage    SMALLINT NOT NULL CHECK (dosage IN (0, 1, 2)),
    PRIMARY KEY (sample_id, rsid)
);

CREATE INDEX IF NOT EXISTS genotypes_rsid_idx ON genotypes (rsid);
CREATE INDEX IF NOT EXISTS genotypes_sample_id_idx ON genotypes (sample_id);
CREATE INDEX IF NOT EXISTS samples_super_pop_idx ON samples (super_population);

-- Manually curated non-medical SNP–trait correlations from the GWAS Catalog.
-- Association = correlation in research cohorts, NOT proven causation for any individual.
CREATE TABLE IF NOT EXISTS trait_associations (
    rsid                      VARCHAR NOT NULL REFERENCES variants (rsid),
    trait_name                VARCHAR NOT NULL,
    effect_allele             CHAR(1) NOT NULL,   -- allele linked to the reported effect direction
    effect_direction          VARCHAR(4) NOT NULL
        CHECK (effect_direction IN ('risk', 'protective', 'other')),
        -- 'risk' here means "associated with a higher trait measurement" (NOT disease risk).
        -- 'protective' means "associated with a lower trait measurement".
        -- 'other' means categorical / no numeric up-down scoring.
    plain_english_description TEXT NOT NULL,
    source                    VARCHAR NOT NULL,   -- e.g. 'GWAS Catalog'
    PRIMARY KEY (rsid, trait_name)
);
