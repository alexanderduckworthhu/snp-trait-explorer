"""
SNP Trait Explorer dashboard.

SNP = a common single-letter DNA difference between people.
See docs/CONCEPTS.md for the plain-English glossary.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

import constants as C
from ml.trait_score import trait_scores_from_dosages
from src import charts, styles
from src.associations import load_associations
from src.db import database_url, read_sql
from src.genotype_session import clear_genotype, has_genotype, render_uploader
from src.i18n import (
    LANGUAGE_LABELS,
    SUPPORTED_LANGS,
    copy_count_phrase,
    dosage_result_label,
    normalize_lang,
    population_label,
    t,
    tf,
)
from src.parsers import dosages_against_associations

ROOT = Path(__file__).resolve().parent
MODELS_DIR = ROOT / "models"
OUTPUTS_DIR = ROOT / "outputs"
MODEL_PATH = MODELS_DIR / "ancestry_clf.joblib"
FEATURE_NAMES_PATH = MODELS_DIR / "feature_names.json"
FEATURE_IMPORTANCES_PATH = OUTPUTS_DIR / "feature_importances.csv"

LOGGER = logging.getLogger(__name__)

st.set_page_config(
    page_title="SNP Trait Explorer",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_resource
def load_ancestry_model() -> tuple[RandomForestClassifier | None, dict[str, Any] | None]:
    """Load the committed ancestry classifier and feature metadata from disk."""
    if not MODEL_PATH.exists() or not FEATURE_NAMES_PATH.exists():
        return None, None
    try:
        classifier = joblib.load(MODEL_PATH)
        metadata = json.loads(FEATURE_NAMES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        LOGGER.exception("Failed to load ancestry model: %s", exc)
        return None, None
    return classifier, metadata


@st.cache_data(ttl=C.DB_CACHE_TTL_SECONDS)
def load_sample_counts() -> pd.DataFrame:
    """Return sample counts by super-population (Postgres or demo panel totals)."""
    demo = pd.DataFrame(
        {
            "super_population": list(C.DEMO_PANEL_COUNTS.keys()),
            "n_samples": list(C.DEMO_PANEL_COUNTS.values()),
        }
    )
    if not database_url():
        return demo
    try:
        return read_sql(
            """
            SELECT super_population, COUNT(*) AS n_samples
            FROM samples
            GROUP BY super_population
            ORDER BY super_population
            """
        )
    except (RuntimeError, ValueError) as exc:
        LOGGER.warning("Falling back to demo sample counts: %s", exc)
        return demo


@st.cache_data(ttl=C.DB_CACHE_TTL_SECONDS)
def load_trait_associations() -> pd.DataFrame:
    """Return curated trait associations from Postgres, or the bundled CSV."""
    fallback = load_associations()
    if not database_url():
        return fallback
    try:
        query_result = read_sql(
            """
            SELECT ta.rsid, ta.trait_name, ta.effect_allele, ta.effect_direction,
                   ta.plain_english_description, ta.source, v.gene_symbol, v.maf
            FROM trait_associations ta
            JOIN variants v ON v.rsid = ta.rsid
            ORDER BY ta.trait_name
            """
        )
        return query_result if not query_result.empty else fallback
    except (RuntimeError, ValueError) as exc:
        LOGGER.warning("Falling back to curated CSV associations: %s", exc)
        return fallback


@st.cache_data(ttl=C.DB_CACHE_TTL_SECONDS)
def load_population_allele_frequencies(rsid: str) -> pd.DataFrame:
    """Return alternate-allele frequency by super-population for one SNP."""
    demo_af = {"AFR": 0.45, "AMR": 0.28, "EAS": 0.12, "EUR": 0.22, "SAS": 0.25}
    seed = sum(ord(character) for character in rsid) % 17

    def _demo_frequencies() -> pd.DataFrame:
        return pd.DataFrame(
            [
                {
                    "super_population": pop,
                    "alt_allele_frequency": round(
                        min(0.49, max(0.02, frequency + (seed - 8) * 0.005)),
                        3,
                    ),
                }
                for pop, frequency in demo_af.items()
            ]
        )

    if not database_url():
        return _demo_frequencies()
    try:
        return read_sql(
            """
            SELECT
                s.super_population,
                ROUND(AVG(g.dosage) / 2.0, 4) AS alt_allele_frequency
            FROM genotypes g
            JOIN samples s ON s.sample_id = g.sample_id
            WHERE g.rsid = %s
            GROUP BY s.super_population
            ORDER BY s.super_population
            """,
            params=(rsid,),
        )
    except (RuntimeError, ValueError) as exc:
        LOGGER.warning("Falling back to demo allele frequencies for %s: %s", rsid, exc)
        return _demo_frequencies()


def _with_population_labels(frame: pd.DataFrame, lang: str) -> pd.DataFrame:
    """Attach localized super-population labels to a dataframe."""
    labeled = frame.copy()
    labeled["label"] = labeled["super_population"].map(
        lambda code: population_label(str(code), lang)
    )
    return labeled


def page_explore(lang: str) -> None:
    """Render the public-data exploration page."""
    st.header(t("page_explore", lang))
    st.caption(t("explore_intro", lang))

    counts = _with_population_labels(load_sample_counts(), lang)
    associations = load_trait_associations()

    tab_overview, tab_snp = st.tabs(
        [t("explore_tab_overview", lang), t("explore_tab_snp", lang)]
    )

    with tab_overview:
        col_counts, col_map = st.columns(2, gap="large")
        with col_counts:
            charts.show(charts.sample_counts_bar(counts, lang))
        with col_map:
            charts.show(charts.ancestry_map(counts, lang), interactive_map=True)
            st.caption(t("explore_map_note", lang))

        maf_column = "maf" if "maf" in associations.columns else "demo_maf"
        maf_values = (
            associations[maf_column].dropna()
            if maf_column in associations.columns
            else pd.Series(dtype=float)
        )
        if maf_values.empty and "demo_maf" in associations.columns:
            maf_values = associations["demo_maf"]
        charts.show(charts.maf_histogram(maf_values, lang))

    with tab_snp:
        st.caption(t("explore_snp_caption", lang))
        marker_options = {
            f"{row.rsid} · {row.trait_name}": row.rsid
            for row in associations.itertuples()
        }
        selected_label = st.selectbox(
            t("marker_select", lang),
            options=list(marker_options.keys()),
        )
        selected_rsid = marker_options[selected_label]
        population_af = _with_population_labels(
            load_population_allele_frequencies(selected_rsid),
            lang,
        )
        charts.show(charts.allele_freq_bar(population_af, selected_rsid, lang))


def page_trait_profile(lang: str) -> None:
    """Render the educational trait profile for an uploaded genotype file."""
    st.header(t("page_trait", lang))
    styles.notice(t("disclaimer_general", lang))

    genotypes = render_uploader("trait_upload", lang)
    if genotypes is None:
        return

    associations = load_trait_associations()
    with st.spinner(t("building_profile", lang)):
        dosages = dosages_against_associations(genotypes, associations)
        scores = trait_scores_from_dosages(dosages, associations)
        matched_count = int(genotypes["rsid"].isin(set(associations["rsid"])).sum())

    st.success(tf("markers_found", lang, n=matched_count))
    st.caption(t("trait_intro", lang))
    st.markdown(
        f'<p class="ste-fade">{t("trait_done", lang)}</p>',
        unsafe_allow_html=True,
    )

    columns = st.columns(3)
    for index, row in enumerate(scores.itertuples()):
        with columns[index % 3]:
            st.markdown(
                styles.trait_card_html(
                    row.rsid,
                    row.trait_name,
                    dosage_result_label(int(row.dosage), lang),
                    row.plain_english_description,
                    delay=(index % 3) + 1,
                ),
                unsafe_allow_html=True,
            )


def page_ancestry(lang: str) -> None:
    """Render the ancestry estimate page for the shared genotype upload."""
    st.header(t("page_ancestry", lang))
    styles.notice(t("disclaimer_ancestry", lang))
    st.caption(t("ancestry_intro", lang))

    classifier, metadata = load_ancestry_model()
    if classifier is None or metadata is None:
        st.error(t("model_missing", lang))
        return

    genotypes = render_uploader("ancestry_upload", lang)
    if genotypes is None:
        if not has_genotype():
            st.info(t("ancestry_need_file", lang))
        return

    feature_names: list[str] = metadata["feature_names"]
    associations = load_trait_associations()

    with st.spinner(t("comparing_ancestry", lang)):
        dosages = dosages_against_associations(genotypes, associations)
        feature_matrix = pd.DataFrame(
            [{rsid: dosages.get(rsid, 0) for rsid in feature_names}]
        )[feature_names]
        class_probabilities = classifier.predict_proba(feature_matrix)[0]
        predicted_code = classifier.predict(feature_matrix)[0]

        if FEATURE_IMPORTANCES_PATH.exists():
            try:
                importance_table = pd.read_csv(FEATURE_IMPORTANCES_PATH)
                importance_by_rsid = dict(
                    zip(importance_table["rsid"], importance_table["rf_importance"])
                )
            except (OSError, ValueError, KeyError) as exc:
                LOGGER.warning("Could not read feature importances CSV: %s", exc)
                importance_by_rsid = dict(
                    zip(feature_names, classifier.feature_importances_)
                )
        else:
            importance_by_rsid = dict(
                zip(feature_names, classifier.feature_importances_)
            )

        gene_by_rsid = dict(zip(associations["rsid"], associations["gene_symbol"]))
        contribution_table = pd.DataFrame(
            [
                {
                    "rsid": rsid,
                    "gene_symbol": gene_by_rsid.get(rsid),
                    "dosage": dosages.get(rsid, 0),
                    "contribution": float(importance_by_rsid.get(rsid, 0.0))
                    * dosages.get(rsid, 0),
                }
                for rsid in feature_names
            ]
        ).sort_values("contribution", ascending=False)

    predicted_label = population_label(str(predicted_code), lang)
    styles.result_metric(
        t("ancestry_result", lang),
        f"{predicted_label} ({predicted_code})",
    )

    probability_table = pd.DataFrame(
        {
            "super_population": classifier.classes_,
            "probability": class_probabilities,
        }
    )
    probability_table = _with_population_labels(probability_table, lang)
    charts.show(charts.probability_bar(probability_table, lang))
    charts.show(charts.contribution_bar(contribution_table, lang))

    st.markdown(f"**{t('ancestry_top3', lang)}**")
    for _, driver in contribution_table.head(C.TOP_DRIVER_COUNT).iterrows():
        dosage = int(driver["dosage"])
        gene_name = driver["gene_symbol"] or t("gene_fallback", lang)
        st.write(
            tf(
                "ancestry_driver_line",
                lang,
                rsid=driver["rsid"],
                gene=gene_name,
                copies=copy_count_phrase(dosage, lang),
            )
        )


def page_methods(lang: str) -> None:
    """Render methods, sources, glossary, and limits."""
    st.header(t("page_methods", lang))
    st.caption(t("about_intro", lang))
    styles.notice(t("disclaimer_general", lang))

    st.markdown(f"### {t('methods_heading', lang)}")
    st.markdown(t("methods_md", lang))

    st.markdown(f"### {t('sources_heading', lang)}")
    st.markdown(t("sources_md", lang))

    st.markdown(f"### {t('limits_heading', lang)}")
    st.markdown(t("limits_md", lang))

    with st.expander(t("glossary_heading", lang), expanded=False):
        st.markdown(t("glossary_md", lang))


def main() -> None:
    """Run the multi-page Streamlit application."""
    styles.inject()

    with st.sidebar:
        previous_lang = normalize_lang(st.session_state.get("ui_lang", "en"))
        st.markdown(f"### {t('lang', previous_lang)}")
        language_code = st.selectbox(
            t("lang", previous_lang),
            options=list(SUPPORTED_LANGS),
            format_func=lambda code: LANGUAGE_LABELS.get(code, code),
            key="ui_lang",
            label_visibility="collapsed",
        )
        lang = normalize_lang(language_code)
        styles.apply_direction(lang)
        st.caption(t("sidebar_hint", lang))
        st.caption(t("sidebar_guide", lang))
        st.caption(t("disclaimer_general", lang))
        if database_url():
            st.success(t("db_connected", lang))
        else:
            st.info(t("db_demo", lang))
        if has_genotype():
            st.caption(t("file_ready_sidebar", lang))
            if st.button(t("reset_session", lang), type="secondary"):
                clear_genotype()
                st.rerun()

    st.markdown(
        f"""
        <div class="ste-hero ste-fade">
          <h1>{t("title", lang)}</h1>
          <p>{t("subtitle", lang)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption(t("snp_glossary", lang))

    if "nav_page_key" not in st.session_state:
        st.session_state["nav_page_key"] = "explore"
    page_keys = ("explore", "trait", "ancestry", "methods")

    nav_cols = st.columns(len(page_keys), gap="small")
    for column, page_key in zip(nav_cols, page_keys):
        is_active = st.session_state["nav_page_key"] == page_key
        with column:
            if st.button(
                t(f"page_{page_key}", lang),
                key=f"nav_btn_{page_key}",
                type="primary" if is_active else "secondary",
                width="stretch",
            ):
                st.session_state["nav_page_key"] = page_key
                st.rerun()

    selected_key = st.session_state["nav_page_key"]
    st.divider()

    if selected_key == "explore":
        page_explore(lang)
    elif selected_key == "trait":
        page_trait_profile(lang)
    elif selected_key == "ancestry":
        page_ancestry(lang)
    else:
        page_methods(lang)


if __name__ == "__main__":
    main()
