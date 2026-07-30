"""Thin Postgres helpers. App fallback associations live in src/associations.py."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def database_url() -> str | None:
    """Return DATABASE_URL from the environment, or None if unset."""
    return os.environ.get("DATABASE_URL")


def connect() -> Any:
    """Open a psycopg2 connection using DATABASE_URL."""
    try:
        import psycopg2
    except ImportError as exc:
        raise RuntimeError("psycopg2 is required for database access") from exc
    url = database_url()
    if not url:
        raise RuntimeError("DATABASE_URL is not set")
    return psycopg2.connect(url)


def read_sql(sql: str, params: Any = None) -> pd.DataFrame:
    """Run a SQL query and return a pandas DataFrame."""
    try:
        import psycopg2
    except ImportError as exc:
        raise RuntimeError("psycopg2 is required for database access") from exc

    connection = connect()
    try:
        return pd.read_sql(sql, connection, params=params)
    except psycopg2.Error as exc:
        raise RuntimeError(f"Postgres query failed: {exc}") from exc
    finally:
        connection.close()
