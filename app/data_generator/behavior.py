import random

# ------------------------------------------
# User Personas
# ------------------------------------------

POWER_USER = "Power User"
REGULAR_USER = "Regular User"
CHURNED_USER = "Churned User"


def sessions_per_user(persona: str) -> int:
    """
    Number of sessions generated for each user.
    """

    if persona == POWER_USER:
        return random.randint(80, 150)

    if persona == REGULAR_USER:
        return random.randint(20, 60)

    return random.randint(2, 6)


def active_days(persona: str) -> int:
    """
    Number of days user remains active.
    """

    if persona == POWER_USER:
        return 180

    if persona == REGULAR_USER:
        return random.randint(45, 120)

    return random.randint(2, 5)


def session_hour(persona: str) -> int:
    """
    Preferred login hour.
    """

    if persona == POWER_USER:
        return random.choice([
            8,
            9,
            10,
            14,
            15,
            16,
            20,
            21
        ])

    if persona == REGULAR_USER:
        return random.choice([
            9,
            12,
            18,
            20
        ])

    return random.choice([
        10,
        18
    ])


def session_template(persona: str):

    if persona == POWER_USER:

        templates = [

            [
                "login",
                "dashboard_viewed",
                "project_created",
                "task_created",
                "task_completed",
                "comment_added",
                "file_uploaded",
                "logout"
            ],

            [
                "login",
                "dashboard_viewed",
                "task_created",
                "task_completed",
                "logout"
            ]

        ]

    elif persona == REGULAR_USER:

        templates = [

            [
                "login",
                "dashboard_viewed",
                "task_created",
                "logout"
            ],

            [
                "login",
                "dashboard_viewed",
                "comment_added",
                "logout"
            ]

        ]

    else:

        templates = [

            [
                "login",
                "dashboard_viewed",
                "logout"
            ],

            [
                "login",
                "logout"
            ]

        ]

    return random.choice(templates)