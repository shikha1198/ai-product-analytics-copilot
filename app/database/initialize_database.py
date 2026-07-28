from pathlib import Path

import pandas as pd

from app.database.database import engine, Base
from app.database.models import User, Event

from app.data_generator.generate_users import generate_users
from app.data_generator.generate_events import generate_events


def initialize_database():

    db_path = Path("analytics.db")

    if db_path.exists():
        return

    print("Creating demo database...")

    Base.metadata.create_all(bind=engine)

    users = generate_users()
    events = generate_events(users)

    users.to_sql(
        "users",
        engine,
        if_exists="append",
        index=False,
    )

    events.to_sql(
        "events",
        engine,
        if_exists="append",
        index=False,
    )

    print("Database initialized successfully.")