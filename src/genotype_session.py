"""Shared genotype upload state so Trait profile and Ancestry reuse one file."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

from src.i18n import tf, t
from src.parsers import parse_upload

ROOT = Path(__file__).resolve().parents[1]
SAMPLE_PATH = ROOT / "data" / "sample" / "demo_genotypes.txt"

STATE_NAME = "genotype_filename"
STATE_BYTES = "genotype_bytes"
STATE_FRAME = "genotype_frame"


def has_genotype() -> bool:
    """Return True when a genotype frame is stored in session state."""
    return st.session_state.get(STATE_FRAME) is not None


def clear_genotype() -> None:
    """Remove the shared genotype upload from session state."""
    for key in (STATE_NAME, STATE_BYTES, STATE_FRAME):
        st.session_state.pop(key, None)


def store_genotype(name: str, raw: bytes, frame: pd.DataFrame) -> None:
    """Persist an uploaded genotype file in session state for reuse across pages."""
    st.session_state[STATE_NAME] = name
    st.session_state[STATE_BYTES] = raw
    st.session_state[STATE_FRAME] = frame


def current_frame() -> pd.DataFrame | None:
    """Return the stored genotype DataFrame, if any."""
    return st.session_state.get(STATE_FRAME)


def current_name() -> str | None:
    """Return the stored genotype filename, if any."""
    return st.session_state.get(STATE_NAME)


def load_sample() -> None:
    """Load the bundled demo genotype file into session state."""
    try:
        raw = SAMPLE_PATH.read_bytes()
        frame = parse_upload(SAMPLE_PATH.name, raw)
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        raise RuntimeError(f"Could not load sample genotype file: {exc}") from exc
    store_genotype(SAMPLE_PATH.name, raw, frame)


def render_uploader(widget_key: str, lang: str) -> pd.DataFrame | None:
    """Render sample/upload controls and return the genotype frame when ready."""
    if has_genotype():
        left, right = st.columns([4, 1])
        with left:
            st.success(tf("file_ready", lang, name=current_name()))
        with right:
            if st.button(t("clear_file", lang), key=f"clear_{widget_key}"):
                clear_genotype()
                st.rerun()
        return current_frame()

    st.caption(t("upload_empty", lang))
    primary, secondary = st.columns([2, 1])
    with primary:
        if st.button(t("sample_button", lang), type="primary", key=f"sample_{widget_key}"):
            with st.spinner(t("reading_file", lang)):
                try:
                    load_sample()
                except RuntimeError:
                    st.error(t("parse_error", lang))
                    return None
            st.toast(t("sample_loaded", lang))
            st.rerun()
    with secondary:
        st.caption(t("or_upload", lang))

    uploaded = st.file_uploader(
        t("upload_label", lang),
        type=["txt", "csv"],
        key=widget_key,
        help=t("upload_help", lang),
    )
    if uploaded is None:
        return None

    with st.spinner(t("reading_file", lang)):
        try:
            frame = parse_upload(uploaded.name, uploaded.getvalue())
        except (ValueError, UnicodeDecodeError, pd.errors.ParserError):
            st.error(t("parse_error", lang))
            return None

    if frame is None or frame.empty:
        st.error(t("parse_empty", lang))
        return None

    store_genotype(uploaded.name, uploaded.getvalue(), frame)
    st.rerun()
    return None
