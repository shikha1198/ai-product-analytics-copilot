import streamlit as st

from app.ai.router import route_question
from app.ai.chart_selector import create_chart
from app.ai.summarizer import summarize


def render_ai_tab():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.subheader("💬 AI Copilot")

    st.caption(
        "Ask questions about your product analytics or uploaded documents."
    )

    question = st.text_input(
        "Ask a question",
        placeholder="e.g. Show DAU trend or What does the SQL guide teach?",
    )

    st.markdown("### ⚡ Suggested Questions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📈 Show DAU Trend"):
            question = "Show DAU trend"

        if st.button("🌍 Top Countries"):
            question = "Show top 10 countries by active users"

        if st.button("🚀 Funnel"):
            question = "Show product funnel"

    with col2:

        if st.button("📊 Feature Adoption"):
            question = "Show feature adoption"

        if st.button("📈 Growth"):
            question = "Show growth accounting"

        if st.button("🔥 Stickiness"):
            question = "Show stickiness"

    ask = st.button(
        "🚀 Ask AI",
        type="primary",
    )

    if ask or question:

        if question.strip():

            result = route_question(question)

            # -----------------------------
            # RAG Answer
            # -----------------------------

            if isinstance(result, str):

                st.subheader("📚 AI Answer")

                st.success(result)

            # -----------------------------
            # Analytics Answer
            # -----------------------------

            else:

                st.success("✅ Query executed successfully!")

                chart = create_chart(result)

                if chart is not None:

                    st.subheader("📊 Visualization")

                    st.plotly_chart(
                        chart,
                        use_container_width=True,
                        key="ai_chart",
                    )

                st.subheader("📋 Raw Data")

                st.dataframe(
                    result,
                    use_container_width=True,
                )

                with st.spinner("🤖 Generating executive summary..."):

                    summary = summarize(
                        question,
                        result,
                    )

                st.subheader("🤖 Executive Summary")

                st.markdown(summary)

                st.session_state.messages.append(
                    {
                        "question": question,
                        "summary": summary,
                        "result": result,
                    }
                )

    # -----------------------------
    # History
    # -----------------------------

    if st.session_state.messages:

        st.divider()

        st.subheader("📝 Previous Conversations")

        for i, message in enumerate(reversed(st.session_state.messages)):

            with st.expander(message["question"]):

                st.markdown(message["summary"])

                history_chart = create_chart(
                    message["result"]
                )

                if history_chart is not None:

                    st.plotly_chart(
                        history_chart,
                        use_container_width=True,
                        key=f"history_{i}",
                    )

                st.dataframe(
                    message["result"],
                    use_container_width=True,
                )