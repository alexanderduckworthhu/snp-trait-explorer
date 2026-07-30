-- Question: For each curated trait, how many samples carry the effect allele
--           (dosage >= 1), and what share is that within each super-population?
-- Biological meaning: The effect allele is the DNA letter that research papers
--           linked to a higher or lower trait measurement. "Carrier" here means
--           someone has at least one copy — a research label, not a medical
--           diagnosis. Rates differ by ancestry because allele frequencies do.
-- Intermediate SQL concept used: multi-level CTE, LEFT JOIN, COALESCE

WITH traits AS (
    SELECT
        ta.rsid,
        ta.trait_name,
        ta.effect_allele,
        ta.effect_direction,
        v.alt_allele,
        v.ref_allele
    FROM trait_associations ta
    JOIN variants v ON v.rsid = ta.rsid
),
-- Map GWAS effect allele onto our VCF dosage (which counts ALT copies).
-- If effect allele == ALT, carriers are dosage >= 1.
-- If effect allele == REF, carriers are people with dosage <= 1 (i.e. not ALT/ALT only
-- would be wrong) — more precisely: copies of effect = 2 - dosage when effect is REF.
carrier_flags AS (
    SELECT
        t.rsid,
        t.trait_name,
        t.effect_direction,
        s.sample_id,
        s.super_population,
        g.dosage AS alt_dosage,
        CASE
            WHEN t.effect_allele = t.alt_allele THEN g.dosage
            WHEN t.effect_allele = t.ref_allele THEN (2 - g.dosage)
            ELSE NULL  -- allele mismatch vs VCF; treat as unknown
        END AS effect_dosage
    FROM traits t
    LEFT JOIN genotypes g ON g.rsid = t.rsid
    LEFT JOIN samples s ON s.sample_id = g.sample_id
),
by_pop AS (
    SELECT
        rsid,
        trait_name,
        effect_direction,
        super_population,
        COUNT(*) FILTER (WHERE effect_dosage >= 1) AS n_carriers,
        COUNT(*) FILTER (WHERE effect_dosage IS NOT NULL) AS n_genotyped
    FROM carrier_flags
    GROUP BY rsid, trait_name, effect_direction, super_population
)
SELECT
    rsid,
    trait_name,
    effect_direction,
    COALESCE(super_population, 'UNKNOWN') AS super_population,
    COALESCE(n_carriers, 0) AS n_carriers,
    COALESCE(n_genotyped, 0) AS n_genotyped,
    ROUND(
        100.0 * COALESCE(n_carriers, 0) / NULLIF(COALESCE(n_genotyped, 0), 0),
        2
    ) AS carrier_pct
FROM by_pop
ORDER BY trait_name, super_population;
