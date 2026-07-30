-- Question: For the 15 curated trait SNPs, how many people in each
--           super-population have dosage 0, 1, or 2 — and which populations
--           carry the most alternate alleles overall?
-- Biological meaning: Dosage is the number of alternate DNA letters someone
--           carries at a SNP (0, 1, or 2). Under Hardy-Weinberg equilibrium
--           (a simple null model: mating is random and nothing distorts allele
--           counts), genotype shares should be roughly (1-p)^2, 2p(1-p), p^2
--           for dosages 0/1/2 — real data is often close but not exact,
--           especially with population structure.
-- Intermediate SQL concept used: CTE → aggregation → PERCENT_RANK() window

WITH trait_snps AS (
    SELECT DISTINCT rsid
    FROM trait_associations
),
dosage_counts AS (
    SELECT
        g.rsid,
        s.super_population,
        g.dosage,
        COUNT(*) AS n_people
    FROM genotypes g
    JOIN samples s ON s.sample_id = g.sample_id
    JOIN trait_snps t ON t.rsid = g.rsid
    GROUP BY g.rsid, s.super_population, g.dosage
),
with_pct AS (
    SELECT
        rsid,
        super_population,
        dosage,
        n_people,
        ROUND(
            100.0 * n_people / SUM(n_people) OVER (
                PARTITION BY rsid, super_population
            ),
            2
        ) AS pct_within_population
    FROM dosage_counts
),
pop_burden AS (
    -- Alternate-allele burden = mean dosage across trait SNPs in that population
    SELECT
        s.super_population,
        ROUND(AVG(g.dosage)::numeric, 4) AS mean_alt_dosage,
        PERCENT_RANK() OVER (ORDER BY AVG(g.dosage)) AS burden_percent_rank
    FROM genotypes g
    JOIN samples s ON s.sample_id = g.sample_id
    JOIN trait_snps t ON t.rsid = g.rsid
    GROUP BY s.super_population
)
SELECT
    w.rsid,
    w.super_population,
    w.dosage,
    w.n_people,
    w.pct_within_population,
    b.mean_alt_dosage,
    ROUND(b.burden_percent_rank::numeric, 3) AS burden_percent_rank
FROM with_pct w
JOIN pop_burden b ON b.super_population = w.super_population
ORDER BY w.rsid, w.super_population, w.dosage;
