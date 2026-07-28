import pandas as pd
from sqlalchemy import text

from app.database.database import engine


def execute_sql(sql: str):

    with engine.connect() as conn:

        df = pd.read_sql(
            text(sql),
            conn,
        )

    return df