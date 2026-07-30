"""Subtle motion and spacing for the Streamlit UI (CSS custom properties)."""

from __future__ import annotations

import streamlit as st

import constants as C

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

:root {{
  --ste-bg: {C.COLOR_BG};
  --ste-surface: {C.COLOR_SURFACE};
  --ste-sidebar: {C.COLOR_SIDEBAR};
  --ste-border: {C.COLOR_BORDER};
  --ste-text: {C.COLOR_TEXT};
  --ste-muted: {C.COLOR_TEXT_MUTED};
  --ste-primary: {C.COLOR_PRIMARY};
  --ste-primary-dark: {C.COLOR_PRIMARY_DARK};
  --ste-accent: {C.COLOR_ACCENT};
  --ste-card: {C.COLOR_CARD_BG};
  --ste-neutral: {C.COLOR_TRAIT_NEUTRAL};
  --ste-nav-idle: {C.COLOR_NAV_IDLE};
  --ste-space-2: {C.SPACE_2};
  --ste-space-3: {C.SPACE_3};
  --ste-space-4: {C.SPACE_4};
  --ste-space-5: {C.SPACE_5};
  --ste-radius-md: {C.RADIUS_MD};
  --ste-radius-lg: {C.RADIUS_LG};
  --ste-font: {C.FONT_UI};
}}

html, body, [class*="css"] {{
  font-family: var(--ste-font);
  color: var(--ste-text);
}}

/* Prevent Streamlit markdown/header collisions with dense layouts */
.block-container {{
  padding-top: 2.75rem !important;
  padding-left: clamp(0.75rem, 2.5vw, 2.5rem) !important;
  padding-right: clamp(0.75rem, 2.5vw, 2.5rem) !important;
  padding-bottom: 2rem !important;
  max-width: 1200px;
  overflow: visible !important;
}}

[data-testid="stMainBlockContainer"],
[data-testid="stVerticalBlock"],
[data-testid="stMarkdownContainer"],
[data-testid="stHeader"],
.stMarkdown {{
  overflow: visible !important;
  min-width: 0 !important;
}}

h1, h2, h3, [data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {{
  font-family: var(--ste-font) !important;
  font-weight: 600 !important;
  letter-spacing: -0.015em;
  color: var(--ste-text) !important;
  line-height: 1.25 !important;
  overflow-wrap: anywhere;
  word-break: break-word;
  hyphens: auto;
  max-width: 100%;
}}

h1, [data-testid="stMarkdownContainer"] h1 {{
  font-size: clamp(1.35rem, 2.8vw + 0.6rem, 2.05rem) !important;
}}
h2, [data-testid="stMarkdownContainer"] h2 {{
  font-size: clamp(1.15rem, 1.6vw + 0.55rem, 1.55rem) !important;
}}
h3, [data-testid="stMarkdownContainer"] h3 {{
  font-size: clamp(1.02rem, 1.1vw + 0.55rem, 1.25rem) !important;
}}

p, li, label, .stCaption, [data-testid="stCaption"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stWidgetLabel"] p {{
  overflow-wrap: break-word;
  word-break: normal;
  max-width: 100%;
}}

.stApp {{
  background:
    radial-gradient(900px 420px at 6% -10%, rgba(26, 95, 173, 0.12) 0%, transparent 55%),
    radial-gradient(700px 360px at 100% 0%, rgba(18, 163, 154, 0.10) 0%, transparent 50%),
    var(--ste-bg);
}}

[data-testid="stSidebar"] {{
  background: linear-gradient(180deg, var(--ste-sidebar) 0%, #D5E2EF 100%);
  border-right: 1px solid var(--ste-border);
}}

.ste-fade {{ animation: steFade 0.4s ease-out both; }}
.ste-rise {{ animation: steRise 0.45s ease-out both; }}
.ste-rise-delay-1 {{ animation-delay: 0.06s; }}
.ste-rise-delay-2 {{ animation-delay: 0.12s; }}
.ste-rise-delay-3 {{ animation-delay: 0.18s; }}

@keyframes steFade {{
  from {{ opacity: 0; }}
  to {{ opacity: 1; }}
}}
@keyframes steRise {{
  from {{ opacity: 0; transform: translateY(6px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}

.ste-hero {{
  padding: 0 0 var(--ste-space-3) 0;
  margin-bottom: var(--ste-space-2);
  max-width: 100%;
}}
.ste-hero h1 {{
  margin: 0 0 var(--ste-space-2) 0 !important;
  line-height: 1.2 !important;
  font-size: clamp(1.35rem, 2.8vw + 0.6rem, 2.05rem) !important;
  overflow-wrap: anywhere;
  word-break: break-word;
}}
.ste-hero p {{
  color: var(--ste-muted);
  font-size: clamp(0.92rem, 0.6vw + 0.8rem, 1.02rem);
  margin: 0;
  max-width: min(44rem, 100%);
  line-height: 1.55;
  overflow-wrap: anywhere;
  word-break: break-word;
}}

.ste-nav-row {{
  display: flex;
  flex-wrap: wrap;
  gap: var(--ste-space-2);
  background: var(--ste-surface);
  border: 1px solid var(--ste-border);
  border-radius: var(--ste-radius-lg);
  padding: var(--ste-space-3);
  margin: var(--ste-space-3) 0 var(--ste-space-5) 0;
  box-shadow: 0 4px 14px rgba(11, 31, 51, 0.04);
}}

/* Page nav buttons inside the nav row columns */
div[data-testid="stHorizontalBlock"]:has(button[kind="secondary"]),
div[data-testid="stHorizontalBlock"]:has(button[kind="primary"]) {{
  gap: 0.5rem !important;
}}

.ste-note {{
  background: var(--ste-surface);
  border: 1px solid var(--ste-border);
  border-left: 4px solid var(--ste-accent);
  border-radius: var(--ste-radius-md);
  padding: 0.9rem clamp(0.75rem, 2vw, var(--ste-space-4));
  color: var(--ste-text);
  margin: var(--ste-space-2) 0 var(--ste-space-4) 0;
  line-height: 1.45;
  font-size: clamp(0.88rem, 0.4vw + 0.8rem, 0.98rem);
  overflow-wrap: anywhere;
  word-break: break-word;
  animation: steRise 0.4s ease-out both;
}}

.ste-card {{
  background: var(--ste-card);
  border: 1px solid var(--ste-border);
  border-radius: var(--ste-radius-lg);
  padding: clamp(0.75rem, 2vw, var(--ste-space-4));
  margin-bottom: 0.9rem;
  min-height: 0;
  overflow: visible;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  animation: steRise 0.4s ease-out both;
}}
.ste-card:hover {{
  transform: translateY(-2px);
  box-shadow: 0 8px 18px rgba(11, 31, 51, 0.08);
  border-color: var(--ste-primary);
}}
.ste-card .ste-rsid {{
  font-size: clamp(0.68rem, 0.3vw + 0.62rem, 0.72rem);
  color: var(--ste-neutral);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  line-height: 1.3;
  overflow-wrap: anywhere;
}}
.ste-card .ste-title {{
  font-size: clamp(0.92rem, 0.5vw + 0.8rem, 1.02rem);
  font-weight: 600;
  color: var(--ste-text);
  margin: 0.4rem 0;
  line-height: 1.35;
  overflow-wrap: anywhere;
  word-break: break-word;
}}
.ste-card .ste-result {{
  font-size: clamp(0.86rem, 0.4vw + 0.75rem, 0.95rem);
  color: var(--ste-neutral);
  font-weight: 500;
  line-height: 1.35;
  overflow-wrap: anywhere;
}}
.ste-card .ste-body {{
  font-size: clamp(0.8rem, 0.35vw + 0.72rem, 0.86rem);
  color: var(--ste-muted);
  margin-top: 0.7rem;
  line-height: 1.5;
  overflow-wrap: anywhere;
  word-break: break-word;
}}

div.stButton > button {{
  white-space: normal !important;
  height: auto !important;
  border-radius: var(--ste-radius-md) !important;
  font-weight: 500 !important;
  min-height: 2.5rem;
  line-height: 1.25 !important;
  padding-top: 0.55rem !important;
  padding-bottom: 0.55rem !important;
  overflow-wrap: anywhere;
}}
div.stButton > button[kind="primary"],
div.stButton > button[data-testid="baseButton-primary"] {{
  background: var(--ste-primary) !important;
  border: 1px solid var(--ste-primary-dark) !important;
  color: #fff !important;
  font-weight: 600 !important;
}}
div.stButton > button[kind="primary"]:hover,
div.stButton > button[data-testid="baseButton-primary"]:hover {{
  transform: translateY(-1px);
  box-shadow: 0 6px 14px rgba(26, 95, 173, 0.28) !important;
}}

[data-testid="stFileUploader"] {{
  background: rgba(255,255,255,0.75);
  border-radius: var(--ste-radius-lg);
  padding: var(--ste-space-2) var(--ste-space-3) var(--ste-space-3);
}}

.ste-metric {{
  background: var(--ste-surface);
  border: 1px solid var(--ste-border);
  border-radius: var(--ste-radius-lg);
  padding: var(--ste-space-4) 1.15rem;
  animation: steRise 0.4s ease-out both;
  margin-bottom: var(--ste-space-4);
}}
.ste-metric .label {{
  font-size: 0.8rem;
  color: var(--ste-muted);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  line-height: 1.3;
}}
.ste-metric .value {{
  font-size: clamp(1.15rem, 1.2vw + 0.85rem, 1.45rem);
  font-weight: 600;
  color: var(--ste-primary);
  margin-top: var(--ste-space-2);
  line-height: 1.3;
  word-break: break-word;
  overflow-wrap: anywhere;
}}

/* Give Plotly charts vertical room so legends do not collide with titles */
div[data-testid="stPlotlyChart"] {{
  margin-bottom: 1rem;
  min-width: 0;
  max-width: 100%;
  overflow: visible;
}}
div.js-plotly-plot, div.js-plotly-plot .svg-container {{
  max-width: 100% !important;
}}
/* Hide Plotly editable axis text overlays only (keep map/chart hover working) */
div.js-plotly-plot .plugin-editable {{
  display: none !important;
  pointer-events: none !important;
}}

/* Stack narrow columns so titles/charts keep readable width in windowed mode */
@media (max-width: 1100px) {{
  div[data-testid="stHorizontalBlock"] {{
    flex-wrap: wrap !important;
    gap: 0.75rem !important;
  }}
  div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {{
    min-width: min(100%, 320px) !important;
    flex: 1 1 320px !important;
  }}
}}

@media (max-width: 760px) {{
  .block-container {{
    padding-top: 3.25rem !important;
  }}
  div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {{
    min-width: 100% !important;
    flex: 1 1 100% !important;
  }}
  [data-testid="stSidebar"] {{
    min-width: min(100%, 18rem);
  }}
}}

:focus-visible {{
  outline: 2px solid var(--ste-primary) !important;
  outline-offset: 2px !important;
}}

/* Arabic RTL: mirror text flow and list/legend indents; charts stay LTR images */
html[dir="rtl"] body,
html[dir="rtl"] .stApp,
html[dir="rtl"] .block-container {{
  direction: rtl;
  text-align: right;
}}
html[dir="rtl"] [data-testid="stSidebar"] {{
  text-align: right;
}}
html[dir="rtl"] .stMarkdown p,
html[dir="rtl"] .stMarkdown li,
html[dir="rtl"] [data-testid="stMarkdownContainer"] p,
html[dir="rtl"] [data-testid="stMarkdownContainer"] li,
html[dir="rtl"] [data-testid="stCaptionContainer"],
html[dir="rtl"] label,
html[dir="rtl"] h1, html[dir="rtl"] h2, html[dir="rtl"] h3 {{
  text-align: right;
}}
html[dir="rtl"] .ste-hero,
html[dir="rtl"] .ste-hero p,
html[dir="rtl"] .ste-note,
html[dir="rtl"] .ste-card,
html[dir="rtl"] .ste-metric {{
  text-align: right;
}}
html[dir="rtl"] .ste-note {{
  border-left: none;
  border-right: 4px solid var(--ste-accent);
}}
html[dir="rtl"] [data-testid="stMarkdownContainer"] ul,
html[dir="rtl"] [data-testid="stMarkdownContainer"] ol {{
  padding-right: 18px;
  padding-left: 0;
}}
"""


def inject() -> None:
    """Inject global CSS tokens and motion into the Streamlit page."""
    st.markdown(CSS, unsafe_allow_html=True)


def apply_direction(lang: str) -> None:
    """Set the document `dir`/`lang` attributes so Arabic renders right-to-left.

    Runs inside a zero-size embedded iframe and reaches into the parent
    document, since Streamlit's own DOM has no attribute hook for this.
    """
    import streamlit.components.v1 as components

    direction = "rtl" if lang == "ar" else "ltr"
    components.html(
        f"""
        <script>
        (function() {{
          try {{
            const doc = window.parent.document;
            doc.documentElement.setAttribute('dir', '{direction}');
            doc.documentElement.setAttribute('lang', '{lang}');
          }} catch (e) {{}}
        }})();
        </script>
        """,
        height=0,
        width=0,
    )


def notice(text: str) -> None:
    """Render a left-accented informational banner."""
    st.markdown(f'<div class="ste-note">{text}</div>', unsafe_allow_html=True)


def trait_card_html(
    rsid: str,
    title: str,
    result: str,
    body: str,
    delay: int = 0,
) -> str:
    """Return HTML for one neutral trait result card."""
    delay_class = f" ste-rise-delay-{delay}" if delay else ""
    return f"""
    <div class="ste-card{delay_class}">
      <div class="ste-rsid">{rsid}</div>
      <div class="ste-title">{title}</div>
      <div class="ste-result">{result}</div>
      <div class="ste-body">{body}</div>
    </div>
    """


def result_metric(label: str, value: str) -> None:
    """Render a primary result callout (label + value)."""
    st.markdown(
        f"""
        <div class="ste-metric">
          <div class="label">{label}</div>
          <div class="value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
