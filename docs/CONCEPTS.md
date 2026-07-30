# SNP Trait Explorer — Core Concepts

Plain-English biology and data concepts used throughout this project.
Every term below is explained once here; code comments point back to this file
or restate the definition on first use.

---

## 1. What a SNP is and why it matters

A SNP (Single Nucleotide Polymorphism, pronounced “snip”) is a place in DNA
where people commonly differ by a single letter — for example, some people
have an A where others have a G. These single-letter differences are the most
common kind of genetic variation between humans. Most SNPs do nothing
noticeable; a smaller set sits near genes that influence physical traits
(like how tall someone tends to be) or how the body handles everyday substances
(like caffeine or vitamin D). This project uses a curated set of those
well-studied SNPs as a teaching window into personal genomics — not as a
clinical test.

## 2. What the 1000 Genomes Project contains

The 1000 Genomes Project sequenced DNA from roughly 2,500 people from
populations around the world and published the results as open research data.
For each person it records which letter they carry at millions of SNP
positions, plus which population group they belong to (for example European
or East Asian ancestry labels used in research). It is the right dataset for
this project because: (1) it is free and anonymised, (2) it already includes
population labels we can use for ancestry-classification demos, and
(3) chromosome 22 is small enough (~50k common SNPs) to download and load
into PostgreSQL on a laptop.

## 3. What a trait association means (correlation, not causation)

A “trait association” means that in large research studies, people who carry
a particular SNP letter tend, on average, to show a slightly different
measurement of some trait (for example slightly higher circulating vitamin D).
That is a **correlation** found in populations — it does **not** prove the SNP
causes the trait in any one person, and it says nothing about disease diagnosis
or treatment.

**How this app communicates that honestly**

- Every user-facing results page shows a disclaimer that results are educational,
  not medical advice.
- Trait cards use neutral grey only (never red/green “good/bad” colours).
- Copy uses words like “associated with” and “research correlation,” never
  “you will” or “you are at risk of disease.”
- Only non-medical traits are included (height components, hair colour,
  metabolic lab markers such as bilirubin, etc.). No disease-risk SNPs.

## 4. What VCF format is

VCF (Variant Call Format) is the standard text file format for storing genetic
variants. Each row is one position in the genome; columns describe the
chromosome, position, SNP name (rsID), the common reference letter, the
alternate letter, and then one genotype column per person (for example `0|1`
meaning one copy of each letter). The 1000 Genomes chr22 file is a compressed
VCF (`.vcf.gz`) with ~2,500 sample columns.

## 5. Glossary (8 terms)

| Term | Plain-English definition |
|------|--------------------------|
| **SNP** | A common single-letter spelling difference in DNA between people. |
| **Allele** | One of the possible letters at a SNP position (for example A or G). |
| **Genotype** | The pair of alleles a person carries at a SNP (one from each parent), for example AA, AG, or GG. |
| **Variant** | Any DNA difference from the reference sequence; in this project we focus on SNP variants. |
| **Locus** | A specific address on a chromosome (a genomic “location”) where a variant sits. |
| **Population** | A research group of people who share a geographic/ancestry label used in genetic studies (for example GBR = British in England and Scotland). |
| **MAF (minor allele frequency)** | How common the rarer allele is in a group, ranging from just above 0 to 0.5. |
| **rsID** | The public catalogue name for a SNP, always starting with “rs” (for example rs429358). |
