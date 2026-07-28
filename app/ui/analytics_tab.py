import streamlit as st
import plotly.express as px


def render_analytics_tab(
    dau,
    wau,
    mau,
    new_users,
    features,
    funnel,
    stickiness,
    growth,
):

    st.subheader("📊 Executive Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Daily Active Users",
            f"{int(dau.iloc[-1]['dau']):,}",
        )

    with col2:
        st.metric(
            "📅 Weekly Active Users",
            f"{int(wau.iloc[-1]['wau']):,}",
        )

    with col3:
        st.metric(
            "📈 Monthly Active Users",
            f"{int(mau.iloc[-1]['mau']):,}",
        )

    with col4:
        st.metric(
            "🚀 Registered Users",
            f"{int(new_users['new_users'].sum()):,}",
        )

    st.divider()

    st.subheader("📈 Daily Active Users")

    fig = px.line(
        dau,
        x="activity_date",
        y="dau",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.subheader("📅 Weekly Active Users")

    fig = px.line(
        wau,
        x="week",
        y="wau",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.subheader("📈 Monthly Active Users")

    fig = px.line(
        mau,
        x="month",
        y="mau",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.subheader("🚀 Feature Adoption")

    fig = px.bar(
        features,
        x="feature_name",
        y="total_events",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.subheader("🎯 Product Funnel")

    fig = px.funnel(
        funnel,
        x="users",
        y="step",
        text="conversion_percent",
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="inside",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.subheader("🔥 User Stickiness")

    fig = px.line(
        stickiness,
        x="activity_date",
        y="stickiness",
        markers=True,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.subheader("📊 Growth Accounting")

    fig = px.bar(
        growth,
        x="activity_date",
        y=[
            "new_users",
            "returning_users",
            "resurrected_users",
        ],
    )

    fig.update_layout(
        barmode="stack",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )