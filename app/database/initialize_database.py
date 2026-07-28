from sqlalchemy import inspect

from app.database.database import engine, Base
from app.database.models import User, Event

from app.data_generator.generate_users import generate_users
from app.data_generator.generate_events import generate_events


def initialize_database():

    print("===== initialize_database called =====")

    inspector = inspect(engine)

    # If both tables already exist, nothing to do
    if (
        inspector.has_table("users")
        and inspector.has_table("events")
    ):
        print("Database already initialized.")
        return

    print("Creating tables...")

    Base.metadata.create_all(bind=engine)

    print("Generating users...")

    users = generate_users()

    print("Generating events...")

    events = generate_events(users)

    print("Writing users...")

    users.to_sql(
        "users",
        con=engine,
        if_exists="append",
        index=False,
    )

    print("Writing events...")

    events.to_sql(
        "events",
        con=engine,
        if_exists="append",
        index=False,
    )

    print("✅ Database initialized successfully.")