import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
import plotly.express as px

from app.analytics.metrics import (
    calculate_dau,
    calculate_wau,
    calculate_mau,
    calculate_new_users,
    calculate_feature_adoption,
)

st.set_page_config(
    page_title="AI Product Analytics Copilot",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Product Analytics Copilot")

st.divider()

# -------------------------
# Load Data
# -------------------------

dau = calculate_dau()

wau = calculate_wau()

mau = calculate_mau()

new_users = calculate_new_users()

features = calculate_feature_adoption()

# -------------------------
# KPI Row
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Latest DAU",
        int(dau.iloc[-1]["dau"])
    )

with col2:
    st.metric(
        "Latest WAU",
        int(wau.iloc[-1]["wau"])
    )

with col3:
    st.metric(
        "Latest MAU",
        int(mau.iloc[-1]["mau"])
    )

with col4:
    st.metric(
        "Total Users",
        int(new_users["new_users"].sum())
    )

st.divider()

# -------------------------
# DAU
# -------------------------

fig = px.line(
    dau,
    x="activity_date",
    y="dau",
    title="Daily Active Users"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------
# WAU
# -------------------------

fig = px.line(
    wau,
    x="week",
    y="wau",
    title="Weekly Active Users"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------
# MAU
# -------------------------

fig = px.line(
    mau,
    x="month",
    y="mau",
    title="Monthly Active Users"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------
# Feature Adoption
# -------------------------

fig = px.bar(
    features,
    x="feature_name",
    y="total_events",
    title="Feature Adoption"
)

st.plotly_chart(
    fig,
    use_container_width=True
)