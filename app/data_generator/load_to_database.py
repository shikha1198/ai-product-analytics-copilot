import pandas as pd

from app.database.database import engine


def load_csv(csv_file, table_name):

    dataframe = pd.read_csv(csv_file)

    dataframe.to_sql(
        name=table_name,
        con=engine,
        if_exists="append",
        index=False
    )

    print(f"✅ Loaded {len(dataframe):,} rows into {table_name}")


def main():

    load_csv(
        "data/users.csv",
        "users"
    )

    load_csv(
        "data/events.csv",
        "events"
    )


if __name__ == "__main__":
    main()