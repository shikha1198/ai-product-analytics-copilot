from datetime import datetime, timedelta
import random

import pandas as pd
from faker import Faker

fake = Faker()

# -----------------------------
# Configuration
# -----------------------------
NUMBER_OF_USERS = 5000

COUNTRIES = [
    "India",
    "United States",
    "United Kingdom",
    "Germany",
    "Canada",
    "Australia",
    "Singapore"
]

DEVICE_TYPES = [
    "Desktop",
    "Android",
    "iOS"
]

PLANS = [
    "Free",
    "Pro",
    "Enterprise"
]

# User behavior segments
PERSONAS = [
    "Power User",
    "Regular User",
    "Churned User"
]


def random_signup_date():
    """
    Returns a random signup date
    between Jan 1 2026 and Jun 30 2026.
    """

    start_date = datetime(2026, 1, 1)
    end_date = datetime(2026, 6, 30)

    number_of_days = (end_date - start_date).days

    return start_date + timedelta(
        days=random.randint(0, number_of_days)
    )


def choose_persona():
    """
    Probability distribution.

    Power User = 15%

    Regular User = 55%

    Churned User = 30%
    """

    return random.choices(
        PERSONAS,
        weights=[15, 55, 30],
        k=1
    )[0]


def choose_plan(persona):
    """
    Assign plans based on persona.
    """

    if persona == "Power User":
        return random.choices(
            PLANS,
            weights=[20, 60, 20],
            k=1
        )[0]

    if persona == "Regular User":
        return random.choices(
            PLANS,
            weights=[80, 18, 2],
            k=1
        )[0]

    return "Free"


def generate_users():

    users = []

    for user_id in range(1, NUMBER_OF_USERS + 1):

        persona = choose_persona()

        user = {

            "user_id": user_id,

            "name": fake.name(),

            "email": fake.unique.email(),

            "signup_date": random_signup_date(),

            "country": random.choice(COUNTRIES),

            "device_type": random.choice(DEVICE_TYPES),

            "plan": choose_plan(persona),

            "persona": persona

        }

        users.append(user)

    users_df = pd.DataFrame(users)

    return users_df


def main():

    users_df = generate_users()

    print(users_df.head())

    print()

    print(users_df["persona"].value_counts())

    print()

    print(users_df["plan"].value_counts())

    users_df.to_csv(
        "data/users.csv",
        index=False
    )

    print()

    print("✅ users.csv created successfully!")


if __name__ == "__main__":
    main()