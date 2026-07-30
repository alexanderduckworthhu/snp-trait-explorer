"""
Transparent weighted trait scores for one sample.

score = dosage × effect_weight
  effect_weight = +1 if effect_direction = 'risk'       # higher trait measure
                  -1 if effect_direction = 'protective' # lower trait measure
                   0 if 'other'                         # categorical / unscored

A transparent scoring rule is more appropriate here than a black-box ML model
because users can misread trait output as medical advice: every number must be
auditable in one sentence ("one copy of the effect allele → score +1"), and a
learned regressor would invent confidence we cannot ethically claim from 15 SNPs.
"""

from __future__ import annotations

import os

import pandas as pd


WEIGHTS = {"risk": 1, "protective": -1, "other": 0}


def get_conn():
    try:
        import psycopg2
    except ImportError as exc:
        raise SystemExit("Install psycopg2-binary to query Postgres.") from exc
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise SystemExit("Set DATABASE_URL.")
    return psycopg2.connect(url)


def trait_scores_for_sample(sample_id: str, conn=None) -> pd.DataFrame:
    owns_conn = conn is None
    if owns_conn:
        conn = get_conn()

    sql = """
        SELECT
            ta.trait_name,
            ta.rsid,
            ta.effect_direction,
            ta.plain_english_description,
            g.dosage,
            CASE
                WHEN g.dosage = 0 THEN 'Non-carrier'
                WHEN g.dosage = 1 THEN 'One copy'
                WHEN g.dosage = 2 THEN 'Two copies'
                ELSE 'Missing'
            END AS result_label
        FROM trait_associations ta
        LEFT JOIN genotypes g
            ON g.rsid = ta.rsid
           AND g.sample_id = %s
        ORDER BY ta.trait_name
    """
    df = pd.read_sql(sql, conn, params=(sample_id,))
    if owns_conn:
        conn.close()

    df["effect_weight"] = df["effect_direction"].map(WEIGHTS).fillna(0).astype(int)
    df["dosage"] = df["dosage"].fillna(0).astype(int)
    df["score"] = df["dosage"] * df["effect_weight"]
    return df[
        [
            "trait_name",
            "rsid",
            "score",
            "dosage",
            "plain_english_description",
            "result_label",
            "effect_direction",
        ]
    ]


def trait_scores_from_dosages(
    dosage_by_rsid: dict[str, int],
    associations: pd.DataFrame,
) -> pd.DataFrame:
    """Score an uploaded genotype dict against curated associations."""
    rows = []
    for _, row in associations.iterrows():
        dosage = int(dosage_by_rsid.get(row["rsid"], 0))
        weight = WEIGHTS.get(row["effect_direction"], 0)
        if dosage == 0:
            label = "Non-carrier"
        elif dosage == 1:
            label = "One copy"
        elif dosage == 2:
            label = "Two copies"
        else:
            label = "Missing"
        rows.append(
            {
                "trait_name": row["trait_name"],
                "rsid": row["rsid"],
                "score": dosage * weight,
                "dosage": dosage,
                "plain_english_description": row["plain_english_description"],
                "result_label": label,
                "effect_direction": row["effect_direction"],
            }
        )
    return pd.DataFrame(rows)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--sample-id", required=True)
    args = parser.parse_args()
    print(trait_scores_for_sample(args.sample_id).to_string(index=False))
