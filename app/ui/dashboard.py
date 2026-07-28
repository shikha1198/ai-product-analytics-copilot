import sys
from pathlib import Path

# --------------------------------------------------
# Make project root importable
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# --------------------------------------------------
# Imports
# --------------------------------------------------

import streamlit as st

from app.analytics.metrics import (
    calculate_dau,
    calculate_wau,
    calculate_mau,
    calculate_new_users,
    calculate_feature_adoption,
    calculate_funnel,
    calculate_stickiness,
    calculate_growth_accounting,
)

from app.insights.narrative import generate_narrative

from app.ui.sidebar import render_sidebar
from app.ui.styles import load_styles
from app.ui.ai_tab import render_ai_tab
from app.ui.analytics_tab import render_analytics_tab
from app.ui.docs_tab import render_docs_tab
from app.database.initialize_database import initialize_database

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Product Analytics Copilot",
    page_icon="📊",
    layout="wide",
)

# --------------------------------------------------
# Theme
# --------------------------------------------------

load_styles()
render_sidebar()
initialize_database()

st.write("🚀 Initializing database...")

initialize_database()

st.write("✅ Database initialized")

# --------------------------------------------------
# Load Metrics
# --------------------------------------------------

dau = calculate_dau()
wau = calculate_wau()
mau = calculate_mau()

new_users = calculate_new_users()
features = calculate_feature_adoption()
funnel = calculate_funnel()
stickiness = calculate_stickiness()
growth = calculate_growth_accounting()
executive_brief = generate_narrative()

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    """
# 🤖 AI Product Analytics Copilot

### Transform natural language into product insights using AI

Generate SQL, analyze product metrics, visualize trends, search product documentation using Retrieval-Augmented Generation (RAG), and receive executive summaries — all from one intelligent assistant.
"""
)

doc_count = len(list(Path("docs").glob("*.pdf")))

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🤖 AI Model",
        "Qwen 2.5",
    )

with col2:
    st.metric(
        "🗄️ Database",
        "SQLite",
    )

with col3:
    st.metric(
        "📚 Documents",
        doc_count,
    )

st.info(
    """
💡 **Try asking**

• Show DAU trend

• Top countries by active users

• Show feature adoption

• Compare WAU vs MAU

• What does the SQL interview guide teach?

• Explain SQL window functions
"""
)

st.divider()

# --------------------------------------------------
# Executive Brief
# --------------------------------------------------

st.subheader("📋 Executive Brief")

with st.container(border=True):
    st.markdown(executive_brief)

st.divider()

# --------------------------------------------------
# Tabs
# --------------------------------------------------

tab1, tab2, tab3 = st.tabs(
    [
        "🤖 AI Assistant",
        "📈 Analytics Dashboard",
        "📚 Knowledge Base",
    ]
)

with tab1:

    render_ai_tab()

with tab2:

    render_analytics_tab(
        dau,
        wau,
        mau,
        new_users,
        features,
        funnel,
        stickiness,
        growth,
    )

with tab3:

    render_docs_tab()

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Built with ❤️ by Shikha Pathak | Python • Streamlit • Ollama • Qwen 2.5 • SQLite • Plotly • FAISS"
)