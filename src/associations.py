"""
Curated non-medical SNP-trait associations (single source for the app).

SNP = a common single-letter DNA difference between people.
See docs/CONCEPTS.md for the glossary.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

_CSV = Path(__file__).resolve().parents[1] / "data" / "curated" / "trait_associations.csv"


def load_associations() -> pd.DataFrame:
    return pd.read_csv(_CSV)
