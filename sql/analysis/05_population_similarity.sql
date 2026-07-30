-- Question: Which continental super-populations look most genetically similar
--           when we only look at average dosages across the 15 trait SNPs?
-- Biological meaning: Populations that share recent ancestry tend to have
--           more similar allele frequencies. If two groups' average dosages
--           move together across SNPs (high correlation), that pattern is
--           consistent with shared ancestry — it is not a family tree and
--           it is not ethnicity as lived identity.
-- Intermediate SQL concept used: CROSS JOIN of populations, corr() aggregate,
--           self-pair exclusion with WHERE p1 < p2

WITH trait_snps AS (
    SELECT DISTINCT rsid FROM trait_associations
),
pop_mean_dosage AS (
    SELECT
        s.super_population,
        g.rsid,
        AVG(g.dosage)::float8 AS mean_dosage
    FROM genotypes g
    JOIN samples s ON s.sample_id = g.sample_id
    JOIN trait_snps t ON t.rsid = g.rsid
    GROUP BY s.super_population, g.rsid
),
pop_list AS (
    SELECT DISTINCT super_population FROM pop_mean_dosage
)
SELECT
    p1.super_population AS population_a,
    p2.super_population AS population_b,
    ROUND(corr(a.mean_dosage, b.mean_dosage)::numeric, 4) AS dosage_correlation,
    COUNT(*) AS n_snps_compared
FROM pop_list p1
CROSS JOIN pop_list p2
JOIN pop_mean_dosage a
    ON a.super_population = p1.super_population
JOIN pop_mean_dosage b
    ON b.super_population = p2.super_population
   AND b.rsid = a.rsid
WHERE p1.super_population < p2.super_population
GROUP BY p1.super_population, p2.super_population
ORDER BY dosage_correlation DESC;
