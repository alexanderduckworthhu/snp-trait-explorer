"""
SHAP explanations for the ancestry Random Forest.

SHAP values attribute how much each SNP dosage pushed the model toward
(or away from) a predicted super-population for a given person.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
import shap

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)


def get_conn():
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise SystemExit("Set DATABASE_URL.")
    return psycopg2.connect(url)


def load_matrix(conn, feature_names: list[str]) -> pd.DataFrame:
    sql = """
        SELECT s.sample_id, s.super_population, g.rsid, g.dosage
        FROM samples s
        JOIN genotypes g ON g.sample_id = s.sample_id
        WHERE g.rsid = ANY(%s)
    """
    long_df = pd.read_sql(sql, conn, params=(feature_names,))
    wide = long_df.pivot_table(
        index=["sample_id", "super_population"],
        columns="rsid",
        values="dosage",
        aggfunc="mean",
    )
    for col in feature_names:
        if col not in wide.columns:
            wide[col] = 0
        wide[col] = wide[col].fillna(0).astype(int)
    return wide[feature_names]


def main() -> None:
    model_path = MODELS / "ancestry_clf.joblib"
    feat_path = MODELS / "feature_names.json"
    if not model_path.exists() or not feat_path.exists():
        raise SystemExit("Train the model first (ml/train_ancestry_classifier.py).")

    clf = joblib.load(model_path)
    meta = json.loads(feat_path.read_text())
    feature_names = meta["feature_names"]

    conn = get_conn()
    X = load_matrix(conn, feature_names)

    # Optional gene symbols for plain-English interpretation
    genes = pd.read_sql(
        "SELECT rsid, gene_symbol FROM variants WHERE rsid = ANY(%s)",
        conn,
        params=(feature_names,),
    )
    conn.close()
    gene_map = dict(zip(genes["rsid"], genes["gene_symbol"]))

    # TreeExplainer is fast for Random Forest (exact tree path algorithm).
    explainer = shap.TreeExplainer(clf)
    # Use a sample for the beeswarm if the matrix is large
    X_plot = X.sample(n=min(500, len(X)), random_state=42)
    shap_values = explainer.shap_values(X_plot)

    plt.figure()
    shap.summary_plot(shap_values, X_plot, show=False, max_display=15)
    out_png = OUTPUTS / "shap_summary.png"
    plt.tight_layout()
    plt.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Wrote {out_png}")

    # Global importance: mean |SHAP| across classes/samples
    importances = clf.feature_importances_
    imp_df = pd.DataFrame(
        {
            "rsid": feature_names,
            "gene_symbol": [gene_map.get(r) for r in feature_names],
            "rf_importance": importances,
        }
    ).sort_values("rf_importance", ascending=False)
    imp_path = OUTPUTS / "feature_importances.csv"
    imp_df.to_csv(imp_path, index=False)
    print(f"Wrote {imp_path}")

    top5 = imp_df.head(5)
    print("\nTop 5 SNPs by Random Forest importance:")
    print(top5.to_string(index=False))

    # Plain-English sketch using the single top SNP
    top = top5.iloc[0]
    print(
        f"\nThe model relies most heavily on {top['rsid']} near gene "
        f"{top['gene_symbol'] or 'an unannotated locus'}, which varies "
        f"significantly between continental super-populations in 1000 Genomes "
        f"(compare AFR vs EUR allele frequencies in sql/analysis/01_...). "
        f"Exact population contrast depends on your trained run — check "
        f"outputs/feature_importances.csv and the SHAP beeswarm."
    )


if __name__ == "__main__":
    main()
