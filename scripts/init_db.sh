#!/usr/bin/env bash
# Create local Postgres database (PostgreSQL 15+).
set -euo pipefail
DB_NAME="${1:-snp_trait_explorer}"

if ! command -v psql >/dev/null 2>&1; then
  echo "psql was not found on your PATH."
  echo "Install PostgreSQL 15+ (e.g. brew install postgresql@15), then re-run."
  echo "The Streamlit app still works in demo mode without a database."
  exit 1
fi

psql postgres -c "CREATE DATABASE ${DB_NAME};" 2>/dev/null || echo "Database may already exist: ${DB_NAME}"
export DATABASE_URL="${DATABASE_URL:-postgresql://postgres:postgres@localhost:5432/${DB_NAME}}"
psql "$DATABASE_URL" -f "$(dirname "$0")/../sql/schema.sql"
echo "Schema applied. DATABASE_URL=$DATABASE_URL"
