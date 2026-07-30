"""Shared Plotly chart builders with localized titles and per-category colors."""

from __future__ import annotations

from typing import Any

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import constants as C
from src.i18n import t

# Disable Plotly's contenteditable axis handles (they overlap tick labels).
# Hover / pan stay enabled so maps and bars remain interactive.
PLOTLY_CONFIG: dict[str, Any] = {
    "displayModeBar": False,
    "editable": False,
    "edits": {
        "axisTitleText": False,
        "titleText": False,
        "legendText": False,
        "shapePosition": False,
        "annotationPosition": False,
        "annotationText": False,
    },
    "doubleClick": "reset",
    "scrollZoom": False,
    "showTips": False,
}

PLOTLY_CONFIG_MAP: dict[str, Any] = {
    **PLOTLY_CONFIG,
    "scrollZoom": True,
    "displayModeBar": True,
    "modeBarButtonsToRemove": [
        "select2d",
        "lasso2d",
        "autoScale2d",
        "toImage",
        "sendDataToCloud",
    ],
}


def show(fig: go.Figure, *, interactive_map: bool = False) -> None:
    """Render a Plotly figure in Streamlit without editable axis overlays."""
    config = PLOTLY_CONFIG_MAP if interactive_map else PLOTLY_CONFIG
    st.plotly_chart(fig, width="stretch", config=config)


def _wrap_title(text: str, width: int = 34) -> str:
    """Soft-wrap long chart titles so they stay visible in narrow columns."""
    words = text.split()
    if not words:
        return text
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if len(candidate) <= width:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return "<br>".join(lines)


def _layout(fig: go.Figure, title: str | None = None, *, bottom_legend: bool = True) -> go.Figure:
    """Apply shared styling with room for title and optional bottom legend."""
    wrapped = _wrap_title(title) if title else ""
    title_lines = wrapped.count("<br>") + 1 if wrapped else 1
    top_margin = 44 + (18 * max(0, title_lines - 1))
    fig.update_layout(
        title=dict(
            text=wrapped,
            x=0.01,
            xanchor="left",
            y=0.98,
            yanchor="top",
            font=dict(family="Plus Jakarta Sans, sans-serif", size=13, color=C.COLOR_TEXT),
            pad=dict(b=6, t=2),
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=48, r=16, t=top_margin, b=96 if bottom_legend else 48),
        font=dict(family="Plus Jakarta Sans, sans-serif", color=C.COLOR_TEXT, size=11),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.28,
            xanchor="left",
            x=0,
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=10),
            itemsizing="constant",
            traceorder="normal",
        )
        if bottom_legend
        else dict(orientation="v"),
        bargap=0.28,
        hovermode="closest",
        dragmode=False,
    )
    fig.update_xaxes(
        automargin=True,
        fixedrange=True,
        showgrid=False,
        zeroline=False,
        ticks="",
        tickfont=dict(size=10),
        title_standoff=8,
        showspikes=False,
        tickangle=0,
    )
    fig.update_yaxes(
        automargin=True,
        fixedrange=True,
        showgrid=True,
        gridcolor="rgba(11, 31, 51, 0.08)",
        zeroline=False,
        ticks="",
        tickfont=dict(size=10),
        title_standoff=8,
        showspikes=False,
    )
    return fig


def _population_colors(frame: pd.DataFrame) -> list[str]:
    """Return a color list aligned to each row's super-population."""
    return [
        C.SUPER_POP_COLORS.get(str(code), C.COLOR_PRIMARY)
        for code in frame["super_population"]
    ]


def sample_counts_bar(counts: pd.DataFrame, lang: str) -> go.Figure:
    """Bar chart of sample counts by super-population (one color per group)."""
    fig = go.Figure(
        data=[
            go.Bar(
                x=counts["label"],
                y=counts["n_samples"],
                marker=dict(color=_population_colors(counts), line=dict(width=0)),
                hovertemplate="%{x}<br>%{y}<extra></extra>",
                showlegend=False,
            )
        ]
    )
    fig.update_yaxes(title_text=t("chart_people", lang), rangemode="tozero")
    return _layout(fig, t("chart_counts_title", lang), bottom_legend=False)


def ancestry_map(counts: pd.DataFrame, lang: str) -> go.Figure:
    """Illustrative choropleth for research ancestry labels."""
    map_df = counts.copy()
    map_df["iso"] = map_df["super_population"].map(C.SUPER_POP_ISO3)
    color_map = {
        str(row.label): C.SUPER_POP_COLORS.get(str(row.super_population), C.COLOR_PRIMARY)
        for row in map_df.itertuples()
    }
    fig = px.choropleth(
        map_df,
        locations="iso",
        color="label",
        hover_name="label",
        hover_data={"n_samples": True, "iso": False, "label": False},
        color_discrete_map=color_map,
    )
    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>Samples: %{customdata[0]}<extra></extra>",
    )
    fig.update_geos(
        showframe=False,
        showcoastlines=True,
        projection_type="natural earth",
        fitbounds="locations",
        bgcolor="rgba(0,0,0,0)",
        resolution=50,
    )
    map_title = _wrap_title(t("chart_map_title", lang), width=32)
    title_lines = map_title.count("<br>") + 1
    fig.update_layout(
        title=dict(
            text=map_title,
            x=0.01,
            xanchor="left",
            y=0.98,
            yanchor="top",
            font=dict(family="Plus Jakarta Sans, sans-serif", size=13, color=C.COLOR_TEXT),
            pad=dict(b=6, t=2),
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=8, r=8, t=44 + (18 * max(0, title_lines - 1)), b=72),
        # Pan/zoom must stay on for geo plots; hover depends on an active dragmode.
        dragmode="pan",
        hovermode="closest",
        clickmode="event",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.08,
            xanchor="left",
            x=0,
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor=C.COLOR_BORDER,
            borderwidth=1,
            font=dict(size=10),
            title_text="",
        ),
        font=dict(family="Plus Jakarta Sans, sans-serif", color=C.COLOR_TEXT, size=11),
    )
    return fig


def maf_histogram(maf_vals: pd.Series, lang: str) -> go.Figure:
    """Histogram of minor allele frequencies with distinct bin colors."""
    fig = px.histogram(
        maf_vals,
        nbins=C.MAF_HIST_BINS,
        labels={"value": t("chart_maf_x", lang)},
        color_discrete_sequence=[C.COLOR_PRIMARY],
    )
    if fig.data:
        n_bars = len(getattr(fig.data[0], "y", []) or []) or C.MAF_HIST_BINS
        fig.data[0].marker.color = [
            C.CHART_CATEGORY_PALETTE[i % len(C.CHART_CATEGORY_PALETTE)]
            for i in range(n_bars)
        ]
        fig.data[0].marker.line = dict(width=0)
        fig.data[0].showlegend = False
    fig.update_layout(showlegend=False, yaxis_title=t("chart_maf_y", lang))
    return _layout(fig, t("chart_maf_title", lang), bottom_legend=False)


def allele_freq_bar(pop_af: pd.DataFrame, rsid: str, lang: str) -> go.Figure:
    """Alternate-allele frequency by super-population (one color per group)."""
    fig = go.Figure(
        data=[
            go.Bar(
                x=pop_af["label"],
                y=pop_af["alt_allele_frequency"],
                marker=dict(color=_population_colors(pop_af), line=dict(width=0)),
                hovertemplate="%{x}<br>%{y:.3f}<extra></extra>",
                showlegend=False,
            )
        ]
    )
    fig.update_yaxes(
        title_text=t("chart_af_y", lang),
        range=[0, C.ALLELE_FREQ_Y_MAX],
    )
    return _layout(
        fig,
        t("chart_af_title", lang).format(rsid=rsid),
        bottom_legend=False,
    )


def probability_bar(prob_df: pd.DataFrame, lang: str) -> go.Figure:
    """Ancestry class probability bar chart (one color per class)."""
    fig = go.Figure(
        data=[
            go.Bar(
                x=prob_df["label"],
                y=prob_df["probability"],
                marker=dict(color=_population_colors(prob_df), line=dict(width=0)),
                hovertemplate="%{x}<br>%{y:.1%}<extra></extra>",
                showlegend=False,
            )
        ]
    )
    fig.update_yaxes(title_text=t("chart_proba_y", lang), range=[0, 1])
    return _layout(fig, t("ancestry_proba", lang), bottom_legend=False)


def contribution_bar(local_df: pd.DataFrame, lang: str) -> go.Figure:
    """Horizontal bar chart of top SNP contributions (one color per SNP)."""
    top = local_df.head(C.TOP_CONTRIBUTION_BARS).copy().iloc[::-1]
    colors = [
        C.CHART_CATEGORY_PALETTE[i % len(C.CHART_CATEGORY_PALETTE)]
        for i in range(len(top))
    ]
    fig = go.Figure(
        data=[
            go.Bar(
                x=top["contribution"],
                y=top["rsid"],
                orientation="h",
                marker=dict(color=colors, line=dict(width=0)),
                hovertemplate="%{y}<br>%{x:.3f}<extra></extra>",
                showlegend=False,
            )
        ]
    )
    fig.update_xaxes(title_text=t("chart_contrib_x", lang), rangemode="tozero")
    fig = _layout(fig, t("ancestry_drivers", lang), bottom_legend=False)
    fig.update_layout(margin=dict(l=96, r=12, t=max(fig.layout.margin.t or 56, 56), b=48))
    return fig
