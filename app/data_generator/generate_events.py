import random
import uuid
from datetime import timedelta

import pandas as pd

from app.data_generator.behavior import (
    session_hour,
    session_template,
)

FEATURE_MAPPING = {
    "signup": "Authentication",
    "login": "Authentication",
    "dashboard_viewed": "Dashboard",
    "project_created": "Projects",
    "task_created": "Tasks",
    "task_completed": "Tasks",
    "comment_added": "Collaboration",
    "file_uploaded": "Files",
    "invite_sent": "Workspace",
    "settings_updated": "Settings",
    "logout": "Authentication",
}


def daily_return_probability(persona: str, day: int) -> float:
    if day == 0:
        return 1.0

    if persona == "Power User":
        return max(0.90 - (day * 0.003), 0.30)

    if persona == "Regular User":
        return max(0.65 - (day * 0.005), 0.10)

    return max(0.45 - (day * 0.08), 0.0)


def max_lifespan(persona: str) -> int:
    if persona == "Power User":
        return 180
    if persona == "Regular User":
        return random.randint(60, 120)
    return random.randint(5, 10)


def sessions_today(persona: str) -> int:
    if persona == "Power User":
        return random.randint(1, 4)
    if persona == "Regular User":
        return random.randint(1, 2)
    return 1


def append_session(events, event_id, user, session_id, start_time):
    current_time = start_time


    for event_name in session_template(user["persona"]):
        events.append(
            {
                "event_id": event_id,
                "user_id": user["user_id"],
                "session_id": session_id,
                "event_name": event_name,
                "event_timestamp": current_time,
                "feature_name": FEATURE_MAPPING[event_name],
                "device_type": user["device_type"],
                "country": user["country"],
                "event_properties": "{}",
            }
        )
        event_id += 1
        current_time += timedelta(seconds=random.randint(20, 180))

    return event_id


def generate_events(users_df):

    events = []
    event_id = 1

    for _, user in users_df.iterrows():

        signup_date = pd.to_datetime(user["signup_date"])

        # -------------------------------------------------
        # Mandatory signup event (Day 0)
        # -------------------------------------------------

        signup_session = str(uuid.uuid4())

        events.append(
            {
                "event_id": event_id,
                "user_id": user["user_id"],
                "session_id": signup_session,
                "event_name": "signup",
                "event_timestamp": signup_date,
                "feature_name": "Authentication",
                "device_type": user["device_type"],
                "country": user["country"],
                "event_properties": "{}",
            }
        )

        event_id += 1

        # -------------------------------------------------
        # User activity after signup
        # -------------------------------------------------

        lifespan = max_lifespan(user["persona"])

        for day in range(lifespan + 1):

            if random.random() > daily_return_probability(
                user["persona"],
                day,
            ):
                continue

            sessions = sessions_today(
                user["persona"]
            )

            for _ in range(sessions):

                session_id = str(uuid.uuid4())

                start_time = signup_date + timedelta(
                    days=day,
                    hours=session_hour(user["persona"]),
                    minutes=random.randint(0, 59),
                )

                event_id = append_session(
                    events,
                    event_id,
                    user,
                    session_id,
                    start_time,
                )

    return pd.DataFrame(events)


def main():
    users_df = pd.read_csv("data/users.csv")
    events_df = generate_events(users_df)

    events_df.to_csv(
        "data/events.csv",
        index=False,
    )

    print(events_df.head())
    print()
    print(events_df["event_name"].value_counts())
    print()
    print(f"Total Events: {len(events_df):,}")
    print("✅ data/events.csv generated")


if __name__ == "__main__":
    main()
