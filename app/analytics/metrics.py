import pandas as pd
from sqlalchemy import text

from app.database.database import engine

from app.analytics.queries import (
    DAU_QUERY,
    WAU_QUERY,
    MAU_QUERY,
    NEW_USERS_QUERY,
    FEATURE_ADOPTION_QUERY,
    COHORT_RETENTION_QUERY,
    FUNNEL_QUERY,
    STICKINESS_QUERY,
    GROWTH_ACCOUNTING_QUERY,
)


def run_query(query: str) -> pd.DataFrame:
    """
    Execute SQL and return a DataFrame.
    """
    return pd.read_sql(
        text(query),
        con=engine,
    )


# --------------------------------------------------
# Basic Metrics
# --------------------------------------------------

def calculate_dau():
    return run_query(DAU_QUERY)


def calculate_wau():
    return run_query(WAU_QUERY)


def calculate_mau():
    return run_query(MAU_QUERY)


def calculate_new_users():
    return run_query(NEW_USERS_QUERY)


def calculate_feature_adoption():
    return run_query(FEATURE_ADOPTION_QUERY)


# --------------------------------------------------
# Cohort Retention
# --------------------------------------------------

def calculate_cohort_retention():

    df = run_query(COHORT_RETENTION_QUERY)

    df["retention_percent"] = (
        df["active_users"] / df["cohort_size"] * 100
    ).round(2)

    retention_matrix = df.pivot(
        index="cohort_date",
        columns="days_after_signup",
        values="retention_percent",
    )

    retention_matrix = retention_matrix.fillna(0)

    return retention_matrix


def calculate_funnel():

    df = run_query(FUNNEL_QUERY)

    order = [
        "signup",
        "login",
        "dashboard_viewed",
        "task_created",
        "task_completed",
    ]

    labels = {
        "signup": "Signup",
        "login": "Login",
        "dashboard_viewed": "Dashboard Viewed",
        "task_created": "Task Created",
        "task_completed": "Task Completed",
    }

    df["event_name"] = pd.Categorical(
        df["event_name"],
        categories=order,
        ordered=True,
    )

    df = df.sort_values("event_name")

    df["step"] = df["event_name"].map(labels)

    first_step = df.iloc[0]["users"]

    df["conversion_percent"] = (
        df["users"] / first_step * 100
    ).round(2)

    return df[
        [
            "step",
            "users",
            "conversion_percent",
        ]
    ]

def calculate_stickiness():

    return run_query(
        STICKINESS_QUERY
    )
def calculate_growth_accounting():

    return run_query(
        GROWTH_ACCOUNTING_QUERY
    )