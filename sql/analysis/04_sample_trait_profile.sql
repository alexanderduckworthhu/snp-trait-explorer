-- Question: For one person (sample_id), what are their dosages at the 15
--           trait SNPs, in plain English, with carrier labels?
-- Biological meaning: This is the educational "trait report" query. Dosage
--           0/1/2 means zero, one, or two copies of the VCF alternate allele.
--           Labels are descriptive only — correlations from research, not
--           medical advice.
-- Intermediate SQL concept used: parameterised query (%(sample_id)s), CASE

-- psycopg2 usage: cur.execute(sql, {"sample_id": "HG00096"})
-- psql usage:     \set sample_id 'HG00096'  then replace %(sample_id)s manually,
--                 or use: WHERE g.sample_id = :'sample_id' in psql scripts.

SELECT
    ta.trait_name,
    ta.rsid,
    v.gene_symbol,
    g.dosage,
    ta.effect_allele,
    ta.effect_direction,
    ta.plain_english_description,
    ta.source,
    CASE
        WHEN g.dosage = 0 THEN 'Non-carrier'
        WHEN g.dosage = 1 THEN 'One copy'
        WHEN g.dosage = 2 THEN 'Two copies'
        ELSE 'Missing'
    END AS result
FROM trait_associations ta
JOIN variants v ON v.rsid = ta.rsid
LEFT JOIN genotypes g
    ON g.rsid = ta.rsid
   AND g.sample_id = %(sample_id)s
ORDER BY ta.trait_name;
