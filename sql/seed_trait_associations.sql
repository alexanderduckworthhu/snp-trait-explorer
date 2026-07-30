-- SNP Trait Explorer — curated non-medical trait associations on chromosome 22.
--
-- IMPORTANT CONSTRAINTS
-- - All SNPs are on chr22 so they exist in the tutorial VCF.
-- - Classic consumer-genetics examples (earwax rs17822931, bitter taste TAS2R38,
--   eye colour HERC2) live on OTHER chromosomes and are intentionally excluded.
-- - Every row is a large-N GWAS Catalog association (discovery N >> 10,000).
-- - No disease-risk traits. effect_direction 'risk'/'protective' means higher/lower
--   trait measurement in research data — never medical risk.
--
-- Run AFTER ingest.py has loaded the matching rows into variants.
-- gene_symbol / trait_category on variants are updated at the end.

BEGIN;

-- Ensure variant rows exist even if full VCF ingest used a whitelist or filter.
-- Positions are GRCh38 from GWAS Catalog / Ensembl (rsID is the join key to 1000G).
-- Positions below are GRCh38 (GWAS Catalog). ingest.py overwrites position/ref/alt
-- from the GRCh37 1000 Genomes VCF using rsID as the stable join key.
INSERT INTO variants (rsid, chromosome, position, ref_allele, alt_allele, maf, gene_symbol, trait_category)
VALUES
    ('rs4253754',  22, 46219247, 'G', 'A', NULL, 'PPARA',     'body_size'),
    ('rs9616409',  22, 49026812, 'A', 'G', NULL, 'LINC01310', 'body_size'),
    ('rs2294239',  22, 29053489, 'A', 'G', NULL, 'ZNRF3',     'body_size'),
    ('rs5998619',  22, 21591562, 'G', 'A', NULL, 'UBE2L3',    'blood_cell'),
    ('rs2283847',  22, 27785411, 'C', 'T', NULL, 'MN1',       'blood_cell'),
    ('rs2845466',  22, 21892449, 'A', 'C', NULL, 'PPM1F',     'blood_cell'),
    ('rs9608828',  22, 29977438, 'C', 'G', NULL, 'MTMR3',     'metabolism'),
    ('rs6519133',  22, 38700597, 'C', 'T', NULL, 'JOSD1',     'metabolism'),
    ('rs80584',    22, 36159746, 'C', 'T', NULL, 'APOL3',     'metabolism'),
    ('rs2294915',  22, 43945024, 'C', 'T', NULL, 'PNPLA3',    'metabolism'),
    ('rs2074735',  22, 31139886, 'G', 'C', NULL, 'PLA2G3',    'vitamin'),
    ('rs3761422',  22, 24430704, 'T', 'C', NULL, 'ADORA2A',   'lifestyle'),
    ('rs5766576',  22, 45235512, 'A', 'C', NULL, 'KIAA0930',  'appearance'),
    ('rs28360615', 22, 28942668, 'G', 'C', NULL, 'ZNRF3',     'appearance'),
    ('rs2904552',  22, 18918451, 'C', 'T', NULL, 'PRODH',     'bone')
ON CONFLICT (rsid) DO UPDATE SET
    gene_symbol    = EXCLUDED.gene_symbol,
    trait_category = EXCLUDED.trait_category;

INSERT INTO trait_associations (
    rsid, trait_name, effect_allele, effect_direction,
    plain_english_description, source
) VALUES
(
    'rs4253754',
    'Standing height tendency',
    'A',
    'risk',
    'In very large studies, people with the A version of this SNP near the PPARA gene were on average slightly taller. That is a small statistical tendency, not a height prediction for any one person.',
    'GWAS Catalog (PMID 36224396)'
),
(
    'rs9616409',
    'Body mass index tendency',
    'G',
    'risk',
    'Carriers of the G allele at this chromosome-22 SNP showed a tiny average increase in body mass index (BMI) across more than a million research participants.',
    'GWAS Catalog (PMID 36581621)'
),
(
    'rs2294239',
    'Waist-to-hip ratio tendency',
    'A',
    'risk',
    'The A allele near ZNRF3 is correlated with a slightly higher waist-to-hip ratio in large population studies. Think of it as a body-shape average, not a personal measurement.',
    'GWAS Catalog (PMID 30239722)'
),
(
    'rs5998619',
    'Red blood cell size (MCV)',
    'A',
    'risk',
    'People with the A allele near UBE2L3 tend to have slightly larger average red blood cell volume (mean corpuscular volume) in blood-lab research datasets.',
    'GWAS Catalog (PMID 32888493)'
),
(
    'rs2283847',
    'Platelet count tendency',
    'T',
    'risk',
    'The T allele near MN1 is associated with a modestly higher average platelet count in blood samples from nearly a million people.',
    'GWAS Catalog (PMID 40436827)'
),
(
    'rs2845466',
    'Hemoglobin concentration tendency',
    'C',
    'risk',
    'Carrying the C allele at this SNP is correlated with a slightly higher average hemoglobin concentration in large blood-trait studies.',
    'GWAS Catalog (PMID 32888493)'
),
(
    'rs9608828',
    'Bilirubin level tendency',
    'C',
    'risk',
    'The C allele near MTMR3 is linked to slightly higher average bilirubin (a normal blood pigment from red-cell turnover) in population lab data.',
    'GWAS Catalog (PMID 40436827)'
),
(
    'rs6519133',
    'GGT enzyme level tendency',
    'T',
    'risk',
    'The T allele near JOSD1 correlates with slightly higher average GGT (an everyday liver-related enzyme measured in blood panels) in large cohorts.',
    'GWAS Catalog (PMID 40436827)'
),
(
    'rs80584',
    'Alkaline phosphatase tendency',
    'T',
    'risk',
    'People with the T allele near APOL3 showed a small average increase in alkaline phosphatase (a routine blood enzyme) across hundreds of thousands of participants.',
    'GWAS Catalog (PMID 34594039)'
),
(
    'rs2294915',
    'Serum urate tendency',
    'T',
    'risk',
    'The T allele in PNPLA3 is associated with slightly higher average serum urate (the blood form of uric acid) in million-scale genetic studies.',
    'GWAS Catalog (PMID 38658550)'
),
(
    'rs2074735',
    'Vitamin D level tendency',
    'C',
    'risk',
    'Near PLA2G3, this SNP''s C allele correlates with slightly higher average vitamin D (25-hydroxyvitamin D) measurements in large serum studies.',
    'GWAS Catalog (PMID 32242144)'
),
(
    'rs3761422',
    'Alcohol drinks-per-week tendency',
    'C',
    'risk',
    'At ADORA2A (a receptor also studied in caffeine research), the C allele is correlated with a tiny average increase in reported drinks per week. That is a behavioural research association, not a drinking forecast.',
    'GWAS Catalog (PMID 30643251)'
),
(
    'rs5766576',
    'Hair colour component',
    'C',
    'other',
    'Variation at this SNP near KIAA0930 is statistically linked to hair-colour categories in large appearance studies. Colour is polygenic, so one SNP cannot determine hair colour alone.',
    'GWAS Catalog (PMID 30595370)'
),
(
    'rs28360615',
    'Male-pattern baldness tendency',
    'C',
    'risk',
    'The C allele near ZNRF3 is associated with male-pattern baldness categories in UK Biobank-scale appearance studies. Population correlation, not a personal forecast.',
    'GWAS Catalog (PMID 30595370)'
),
(
    'rs2904552',
    'Heel bone mineral density tendency',
    'T',
    'risk',
    'Carriers of the T allele near PRODH showed a slight average difference in heel bone mineral density in a large bone-strength study.',
    'GWAS Catalog (PMID 30595370)'
)

ON CONFLICT (rsid, trait_name) DO UPDATE SET
    effect_allele             = EXCLUDED.effect_allele,
    effect_direction          = EXCLUDED.effect_direction,
    plain_english_description = EXCLUDED.plain_english_description,
    source                    = EXCLUDED.source;

COMMIT;
