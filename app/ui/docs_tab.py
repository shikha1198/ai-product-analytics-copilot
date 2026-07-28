import streamlit as st
from pathlib import Path


def render_docs_tab():

    st.subheader("📚 Product Documentation")

    st.caption(
        "These documents are indexed by the RAG engine and can be queried using natural language."
    )

    docs_path = Path("docs")

    pdfs = list(docs_path.glob("*.pdf"))

    if not pdfs:

        st.warning("No PDF documents found.")

        return

    st.success(f"{len(pdfs)} document(s) indexed.")

    for pdf in pdfs:

        st.markdown(f"📄 **{pdf.name}**")

    st.divider()

    st.info(
        """
Examples:

• What does the SQL interview guide teach?

• Explain window functions.

• What topics are covered in joins?

• Summarize this document.
"""
    )