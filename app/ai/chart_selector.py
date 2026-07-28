import plotly.express as px


def create_chart(df):
    """
    Automatically chooses a visualization
    based on the returned dataframe.
    """

    if df.empty:
        return None

    columns = list(df.columns)

    # ---------- Single column ----------

    if len(columns) < 2:
        return None

    # ---------- Time Series ----------

    if (
        "date" in columns[0].lower()
        or "day" in columns[0].lower()
        or "month" in columns[0].lower()
        or "week" in columns[0].lower()
    ):

        return px.line(
            df,
            x=columns[0],
            y=columns[1],
            markers=True,
        )

    # ---------- Category ----------

    return px.bar(
        df,
        x=columns[0],
        y=columns[1],
        text=columns[1],
    )