import random
import uuid
from datetime import timedelta

import pandas as pd

from app.data_generator.behavior import (
    sessions_per_user,
    active_days,
    session_hour,
    session_template,
)

FEATURE_MAPPING = {
    "login": "Authentication",
    "dashboard_viewed": "Dashboard",
    "project_created": "Projects",
    "task_created": "Tasks",
    "task_completed": "Tasks",
    "comment_added": "Collaboration",
    "file_uploaded": "Files",
    "invite_sent": "Workspace",
    "settings_updated": "Settings",
    "logout": "Authentication"
}


def generate_events(users_df):

    events = []

    event_id = 1

    for _, user in users_df.iterrows():

        signup_date = pd.to_datetime(
            user["signup_date"]
        )

        total_sessions = sessions_per_user(
            user["persona"]
        )

        lifespan = active_days(
            user["persona"]
        )

        for _ in range(total_sessions):

            session_id = str(uuid.uuid4())

            day = random.randint(
                0,
                lifespan
            )

            current_time = signup_date + timedelta(
                days=day,
                hours=session_hour(
                    user["persona"]
                ),
                minutes=random.randint(
                    0,
                    59
                )
            )

            template = session_template(
                user["persona"]
            )

            for event_name in template:

                events.append(

                    {

                        "event_id": event_id,

                        "user_id": user["user_id"],

                        "session_id": session_id,

                        "event_name": event_name,

                        "event_timestamp": current_time,

                        "feature_name": FEATURE_MAPPING[
                            event_name
                        ],

                        "device_type": user[
                            "device_type"
                        ],

                        "country": user[
                            "country"
                        ],

                        "event_properties": "{}"

                    }

                )

                event_id += 1

                current_time += timedelta(

                    seconds=random.randint(
                        20,
                        180
                    )

                )

    return pd.DataFrame(events)


def main():

    users_df = pd.read_csv(
        "data/users.csv"
    )

    events_df = generate_events(
        users_df
    )

    print(events_df.head())

    print()

    print(events_df["event_name"].value_counts())

    print()

    print(f"Total Events: {len(events_df):,}")

    events_df.to_csv(
        "data/events.csv",
        index=False
    )

    print()

    print("✅ data/events.csv generated")


if __name__ == "__main__":
    main()