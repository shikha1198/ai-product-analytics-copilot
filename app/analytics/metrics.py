import pandas as pd

from sqlalchemy import text

from app.database.database import engine

from app.analytics.queries import (
    DAU_QUERY,
    WAU_QUERY,
    MAU_QUERY,
    NEW_USERS_QUERY,
    FEATURE_ADOPTION_QUERY,
)


def run_query(query: str) -> pd.DataFrame:
    """
    Executes SQL and returns
    a pandas DataFrame.
    """

    return pd.read_sql(
        text(query),
        con=engine
    )


def calculate_dau():

    return run_query(
        DAU_QUERY
    )


def calculate_wau():

    return run_query(
        WAU_QUERY
    )


def calculate_mau():

    return run_query(
        MAU_QUERY
    )


def calculate_new_users():

    return run_query(
        NEW_USERS_QUERY
    )


def calculate_feature_adoption():

    return run_query(
        FEATURE_ADOPTION_QUERY
    )