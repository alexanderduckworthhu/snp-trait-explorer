"""Design tokens and non-translatable reference maps for SNP Trait Explorer."""

from __future__ import annotations

# Cache TTL for Postgres-backed dashboard queries (seconds).
DB_CACHE_TTL_SECONDS = 600

# Demo panel counts from 1000 Genomes phase 3 integrated call samples.
DEMO_PANEL_COUNTS: dict[str, int] = {
    "AFR": 661,
    "AMR": 347,
    "EAS": 504,
    "EUR": 503,
    "SAS": 489,
}

# ISO-3 codes for Plotly choropleth (stable vs country-name matching).
SUPER_POP_ISO3: dict[str, str] = {
    "AFR": "NGA",
    "AMR": "MEX",
    "EAS": "JPN",
    "EUR": "GBR",
    "SAS": "IND",
}

# Clinical-lab palette (sapphire + soft cyan), distinct from ICU forest green
# and Where Needs Overlap teal.
COLOR_BG = "#EEF3F8"
COLOR_SURFACE = "#FFFFFF"
COLOR_SIDEBAR = "#E2EAF3"
COLOR_BORDER = "#C5D4E3"
COLOR_TEXT = "#0B1F33"
COLOR_TEXT_MUTED = "#4A6174"
COLOR_PRIMARY = "#1A5FAD"
COLOR_PRIMARY_DARK = "#134A87"
COLOR_ACCENT = "#12A39A"
COLOR_SECONDARY = "#3E5C76"
COLOR_CARD_BG = "#F7FAFD"
COLOR_TRAIT_NEUTRAL = "#5B6E7D"
COLOR_NAV_ACTIVE = "#1A5FAD"
COLOR_NAV_IDLE = "#D7E3EF"

# One distinct color per super-population (and reusable categorical series).
SUPER_POP_COLORS: dict[str, str] = {
    "AFR": "#E07A5F",
    "AMR": "#3D5A80",
    "EAS": "#2A9D8F",
    "EUR": "#E9C46A",
    "SAS": "#7B68A6",
}

CHART_CATEGORY_PALETTE: list[str] = [
    "#1A5FAD",
    "#E07A5F",
    "#2A9D8F",
    "#E9C46A",
    "#7B68A6",
    "#3D5A80",
    "#F4A261",
    "#264653",
    "#9B5DE5",
    "#00BBF9",
    "#00F5D4",
    "#FEE440",
    "#F15BB5",
    "#8AC926",
    "#1982C4",
]

FONT_UI = '"Plus Jakarta Sans", "IBM Plex Sans", "Segoe UI", sans-serif'

SPACE_1 = "4px"
SPACE_2 = "8px"
SPACE_3 = "12px"
SPACE_4 = "16px"
SPACE_5 = "24px"
SPACE_6 = "32px"

RADIUS_MD = "10px"
RADIUS_LG = "12px"

ALLELE_FREQ_Y_MAX = 0.6
MAF_HIST_BINS = 8
TOP_CONTRIBUTION_BARS = 8
TOP_DRIVER_COUNT = 3
