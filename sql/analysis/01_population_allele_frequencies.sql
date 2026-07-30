-- Question: For each SNP, how common is the rarer allele within each
--           continental super-population (AFR, AMR, EAS, EUR, SAS)?
-- Biological meaning: MAF (Minor Allele Frequency) is how common the rarer
--           DNA letter is in a group. The same SNP can be common in one
--           ancestry group and rare in another because populations have
--           different histories. A SNP that looks "rare globally" may still
--           be common in one super-population — so ancestry-aware frequencies
--           matter for fair interpretation and for ML features.
-- Intermediate SQL concept used: GROUP BY with FILTER, ROUND(), HAVING

-- Allele frequency from dosage: mean(dosage)/2
-- because dosage counts copies of the alternate allele (0, 1, or 2).

SELECT
    g.rsid,
    s.super_population,
    COUNT(*) AS n_samples,
    ROUND(AVG(g.dosage) / 2.0, 4) AS alt_allele_frequency,
    ROUND(
        LEAST(AVG(g.dosage) / 2.0, 1.0 - AVG(g.dosage) / 2.0),
        4
    ) AS maf,
    -- FILTER: count only samples with at least one alternate copy
    COUNT(*) FILTER (WHERE g.dosage >= 1) AS n_with_alt_allele,
    COUNT(*) FILTER (WHERE g.dosage = 2) AS n_alt_homozygotes
FROM genotypes g
JOIN samples s ON s.sample_id = g.sample_id
GROUP BY g.rsid, s.super_population
HAVING ROUND(
    LEAST(AVG(g.dosage) / 2.0, 1.0 - AVG(g.dosage) / 2.0),
    4
) > 0.05
ORDER BY g.rsid, s.super_population;
