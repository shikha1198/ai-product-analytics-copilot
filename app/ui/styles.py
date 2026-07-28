import streamlit as st


def load_styles():

    st.markdown(
        """
<style>

/* ---------- Background ---------- */

.stApp{
    background:#F6F8FC;
}

/* ---------- Metric Cards ---------- */

[data-testid="stMetric"]{
    background:white;
    border-radius:18px;
    padding:18px;
    border:1px solid #E5E7EB;
    box-shadow:0 4px 12px rgba(0,0,0,.05);
}

/* ---------- Containers ---------- */

[data-testid="stVerticalBlockBorderWrapper"]{
    border-radius:18px;
    border:1px solid #E5E7EB;
}

/* ---------- Buttons ---------- */

.stButton>button{
    border-radius:12px;
    height:46px;
    width:100%;
    font-weight:600;
}

/* ---------- Input ---------- */

.stTextInput input{
    border-radius:12px;
}

/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"]{
    background:#111827;
}

section[data-testid="stSidebar"] *{
    color:white;
}

</style>
""",
        unsafe_allow_html=True,
    )