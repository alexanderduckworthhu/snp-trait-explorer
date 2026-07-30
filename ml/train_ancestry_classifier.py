"""
Train a Random Forest to predict super-population (AFR/AMR/EAS/EUR/SAS)
from genotype dosages at the 15 curated trait SNPs.

SNP = single-letter DNA difference; dosage = how many alternate copies (0/1/2);
super-population = broad research ancestry label used in 1000 Genomes.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import joblib
import pandas as pd
import psycopg2
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
OUTPUTS = ROOT / "outputs"
MODELS.mkdir(exist_ok=True)
OUTPUTS.mkdir(exist_ok=True)


def get_conn():
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise SystemExit("Set DATABASE_URL before training.")
    return psycopg2.connect(url)


def load_feature_matrix(conn) -> tuple[pd.DataFrame, pd.Series, list[str]]:
    """Wide matrix: one row per sample, one column per SNP dosage."""
    sql = """
        SELECT
            s.sample_id,
            s.super_population,
            g.rsid,
            g.dosage
        FROM samples s
        JOIN genotypes g ON g.sample_id = s.sample_id
        JOIN trait_associations ta ON ta.rsid = g.rsid
    """
    long_df = pd.read_sql(sql, conn)
    if long_df.empty:
        raise SystemExit("No genotype rows for trait SNPs. Run ingest.py first.")

    wide = long_df.pivot_table(
        index=["sample_id", "super_population"],
        columns="rsid",
        values="dosage",
        aggfunc="mean",
    ).reset_index()

    feature_names = sorted(c for c in wide.columns if c.startswith("rs"))
    # Fill rare missing dosages with column mode (most common integer)
    for col in feature_names:
        mode = wide[col].mode(dropna=True)
        fill = int(mode.iloc[0]) if len(mode) else 0
        wide[col] = wide[col].fillna(fill).astype(int)

    y = wide["super_population"]
    X = wide[feature_names]
    return X, y, feature_names


def main() -> None:
    conn = get_conn()
    X, y, feature_names = load_feature_matrix(conn)
    conn.close()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # Random Forest handles genomic dosage data well because SNP effects can be
    # non-linear and interactive, trees are robust when many features are weakly
    # informative or sparse, and feature_importances_ is built-in for explanation.
    clf = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1,
        class_weight="balanced_subsample",
    )
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    # Ancestry prediction from SNPs is relatively easy for ML because continental
    # groups have systematically different allele frequencies — the feature
    # distributions already separate the classes before the model runs.
    print(f"Accuracy: {acc:.3f} (target > 0.90 with real 1000G trait SNPs)")
    print("Confusion matrix (rows=true, cols=pred):")
    labels = sorted(y.unique())
    print(pd.DataFrame(confusion_matrix(y_test, y_pred, labels=labels), index=labels, columns=labels))
    print(classification_report(y_test, y_pred, digits=3))
    print("Macro F1:", f1_score(y_test, y_pred, average="macro"))

    joblib.dump(clf, MODELS / "ancestry_clf.joblib")
    with (MODELS / "feature_names.json").open("w") as fh:
        json.dump({"feature_names": feature_names, "classes": list(clf.classes_)}, fh, indent=2)

    metrics = {
        "accuracy": float(acc),
        "macro_f1": float(f1_score(y_test, y_pred, average="macro")),
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test)),
        "features": feature_names,
    }
    with (OUTPUTS / "ancestry_metrics.json").open("w") as fh:
        json.dump(metrics, fh, indent=2)
    print(f"Saved model → {MODELS / 'ancestry_clf.joblib'}")


if __name__ == "__main__":
    main()
