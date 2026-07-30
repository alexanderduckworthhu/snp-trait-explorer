"""
Train and commit a demo ancestry classifier WITHOUT requiring the full VCF/DB.

Generates synthetic dosages whose allele frequencies differ by super-population
(the same signal that makes real 1000 Genomes ancestry prediction easy), then
saves models/ancestry_clf.joblib so Streamlit Cloud never trains at runtime.
"""

from __future__ import annotations

import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
OUTPUTS = ROOT / "outputs"
MODELS.mkdir(exist_ok=True)
OUTPUTS.mkdir(exist_ok=True)

# Approximate alternate-allele frequencies by super-population for each trait SNP.
# These are illustrative teaching values (not claimed as exact 1000G AF tables).
FEATURE_NAMES = [
    "rs4253754",
    "rs9616409",
    "rs2294239",
    "rs5998619",
    "rs2283847",
    "rs2845466",
    "rs9608828",
    "rs6519133",
    "rs80584",
    "rs2294915",
    "rs2074735",
    "rs3761422",
    "rs5766576",
    "rs28360615",
    "rs2904552",
]

# Rows: populations; cols: SNPs — P(ALT allele).
# Frequencies are intentionally well-separated so the committed demo model
# mirrors the real 1000G lesson: ancestry is easy when allele frequencies differ.
# Each population owns a near-private high-frequency SNP block (cols below).
AF = {
    #           0     1     2     3     4     5     6     7     8     9    10    11    12    13    14
    "AFR": [0.90, 0.85, 0.88, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
    "AMR": [0.05, 0.05, 0.05, 0.90, 0.85, 0.88, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
    "EAS": [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.90, 0.85, 0.88, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
    "EUR": [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.90, 0.85, 0.88, 0.05, 0.05, 0.05],
    "SAS": [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.90, 0.85, 0.88],
}

N_PER_POP = 500


def sample_dosages(p_alt: float, n: int, rng: np.random.Generator) -> np.ndarray:
    """Hardy-Weinberg-ish dosage draw from allele frequency p_alt."""
    # genotype probs: (1-p)^2, 2p(1-p), p^2 → dosages 0,1,2
    p = np.clip(p_alt, 0.01, 0.99)
    probs = [(1 - p) ** 2, 2 * p * (1 - p), p ** 2]
    return rng.choice([0, 1, 2], size=n, p=probs)


def main() -> None:
    rng = np.random.default_rng(42)
    frames = []
    for pop, freqs in AF.items():
        data = {rs: sample_dosages(f, N_PER_POP, rng) for rs, f in zip(FEATURE_NAMES, freqs)}
        df = pd.DataFrame(data)
        df["super_population"] = pop
        frames.append(df)
    data = pd.concat(frames, ignore_index=True)

    X = data[FEATURE_NAMES]
    y = data["super_population"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    clf = RandomForestClassifier(
        n_estimators=40,
        max_depth=8,
        random_state=42,
        n_jobs=1,
    )
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    acc = accuracy_score(y_test, pred)
    print(f"Demo model accuracy: {acc:.3f}")
    print(classification_report(y_test, pred, digits=3))

    joblib.dump(clf, MODELS / "ancestry_clf.joblib")
    with (MODELS / "feature_names.json").open("w") as fh:
        json.dump(
            {
                "feature_names": FEATURE_NAMES,
                "classes": list(clf.classes_),
                "trained_on": "synthetic_demo",
                "note": "Replace by ml/train_ancestry_classifier.py after real ingest for portfolio metrics.",
            },
            fh,
            indent=2,
        )

    # Minimal importance CSV so explain artifacts exist in-repo
    imp = pd.DataFrame(
        {"rsid": FEATURE_NAMES, "rf_importance": clf.feature_importances_}
    ).sort_values("rf_importance", ascending=False)
    gene_map = {
        "rs4253754": "PPARA",
        "rs9616409": "LINC01310",
        "rs2294239": "ZNRF3",
        "rs5998619": "UBE2L3",
        "rs2283847": "MN1",
        "rs2845466": "PPM1F",
        "rs9608828": "MTMR3",
        "rs6519133": "JOSD1",
        "rs80584": "APOL3",
        "rs2294915": "PNPLA3",
        "rs2074735": "PLA2G3",
        "rs3761422": "ADORA2A",
        "rs5766576": "KIAA0930",
        "rs28360615": "ZNRF3",
        "rs2904552": "PRODH",
    }
    imp["gene_symbol"] = imp["rsid"].map(gene_map)
    imp.to_csv(OUTPUTS / "feature_importances.csv", index=False)
    print(f"Saved {MODELS / 'ancestry_clf.joblib'}")


if __name__ == "__main__":
    main()
