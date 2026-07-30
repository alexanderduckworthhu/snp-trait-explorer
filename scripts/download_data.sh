#!/usr/bin/env bash
# Download a manageable 1000 Genomes Project subset (chromosome 22 + sample panel).
# SNP = a common single-letter DNA difference; VCF = the standard file format for variants.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RAW="${ROOT}/data/raw"
mkdir -p "${RAW}"

BASE="http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502"
VCF_NAME="ALL.chr22.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz"
PANEL_NAME="integrated_call_samples_v3.20130502.ALL.panel"

echo "=== Expected sizes (from EBI FTP Content-Length) ==="
echo "  ${VCF_NAME}"
echo "    ~196 MB compressed (205,612,353 bytes)"
echo "  ${VCF_NAME}.tbi  (optional tabix index)"
echo "    ~35 KB"
echo "  ${PANEL_NAME}"
echo "    ~54 KB (55,156 bytes)"
echo

confirm_size() {
  local url="$1"
  local label="$2"
  local bytes
  bytes="$(curl -sI "${url}" | awk -F': ' 'tolower($1)=="content-length"{gsub(/\r/,"",$2); print $2; exit}')"
  if [[ -n "${bytes}" ]]; then
    echo "Confirmed ${label}: ${bytes} bytes (~$(python3 -c "print(round(${bytes}/1024/1024,1))") MB)"
  else
    echo "Warning: could not confirm size for ${label}"
  fi
}

confirm_size "${BASE}/${VCF_NAME}" "chr22 VCF"
confirm_size "${BASE}/${PANEL_NAME}" "sample panel"
echo

cd "${RAW}"

if [[ ! -f "${VCF_NAME}" ]]; then
  echo "Downloading chr22 phased VCF (phase 3)..."
  curl -L --progress-bar -O "${BASE}/${VCF_NAME}"
else
  echo "Already present: ${VCF_NAME}"
fi

if [[ ! -f "${PANEL_NAME}" ]]; then
  echo "Downloading sample panel (population metadata)..."
  curl -L --progress-bar -O "${BASE}/${PANEL_NAME}"
else
  echo "Already present: ${PANEL_NAME}"
fi

# Optional index — useful if you later query with tabix/cyvcf2 region queries.
if [[ ! -f "${VCF_NAME}.tbi" ]]; then
  echo "Downloading tabix index (optional, ~35 KB)..."
  curl -L --progress-bar -O "${BASE}/${VCF_NAME}.tbi" || true
fi

echo
echo "Done. Files in ${RAW}:"
ls -lh "${RAW}/${VCF_NAME}" "${RAW}/${PANEL_NAME}" 2>/dev/null || true
