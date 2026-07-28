import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🤖 AI Copilot")

        st.divider()

        st.subheader("Tech Stack")

        st.markdown("""
- 🐍 Python
- 🗄️ SQLite
- 🤖 Ollama
- 🧠 Qwen 2.5
- 📊 Streamlit
- 📈 Plotly
- 🐼 Pandas
- 📚 RAG + FAISS
""")

        st.divider()

        st.subheader("Capabilities")

        st.success("Natural Language → SQL")
        st.success("Automatic Charts")
        st.success("Executive Summaries")
        st.success("RAG Search")

        st.divider()

        st.caption("Built by Shikha Pathak")