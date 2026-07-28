from sqlalchemy import inspect, text

from app.database.database import engine, Base
from app.database.models import User, Event

from app.data_generator.generate_users import generate_users
from app.data_generator.generate_events import generate_events


def initialize_database():
    print("===== initialize_database called =====")
    print(f"ENGINE URL: {engine.url}")

    inspector = inspect(engine)

    if inspector.has_table("users") and inspector.has_table("events"):
        with engine.connect() as conn:
            users_count = conn.execute(text("SELECT COUNT(*) FROM users")).scalar() or 0
            events_count = conn.execute(text("SELECT COUNT(*) FROM events")).scalar() or 0

        print(f"Existing rows -> users: {users_count}, events: {events_count}")

        if users_count > 0 and events_count > 0:
            print("Database already initialized.")
            return

    print("Creating tables...")
    Base.metadata.create_all(bind=engine)

    with engine.connect() as conn:
        users_count = conn.execute(text("SELECT COUNT(*) FROM users")).scalar() or 0
        events_count = conn.execute(text("SELECT COUNT(*) FROM events")).scalar() or 0

    if users_count > 0 and events_count > 0:
        print("Database already populated.")
        return

    print("Generating users...")
    users = generate_users()

    print("Generating events...")
    events = generate_events(users)

    print(f"Writing {len(users):,} users...")
    users.to_sql(
        "users",
        con=engine,
        if_exists="append",
        index=False,
    )

    print(f"Writing {len(events):,} events...")
    events.to_sql(
        "events",
        con=engine,
        if_exists="append",
        index=False,
    )

    with engine.connect() as conn:
        users_count = conn.execute(text("SELECT COUNT(*) FROM users")).scalar() or 0
        events_count = conn.execute(text("SELECT COUNT(*) FROM events")).scalar() or 0

    print("✅ Database initialized successfully.")
    print(f"Final counts -> users: {users_count}, events: {events_count}")