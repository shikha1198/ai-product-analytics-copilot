from sqlalchemy import inspect

from app.database.database import engine


def main():

    inspector = inspect(engine)

    print("\nTables found:\n")

    for table in inspector.get_table_names():
        print(f"✅ {table}")


if __name__ == "__main__":
    main()