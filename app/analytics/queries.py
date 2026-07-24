"""
All SQL queries used by the Analytics Engine.
"""

# ----------------------------------------------------
# Daily Active Users
# ----------------------------------------------------

DAU_QUERY = """
SELECT

DATE(event_timestamp) AS activity_date,

COUNT(DISTINCT user_id) AS dau

FROM events

GROUP BY DATE(event_timestamp)

ORDER BY activity_date;
"""


# ----------------------------------------------------
# Weekly Active Users
# ----------------------------------------------------

WAU_QUERY = """
SELECT

strftime('%Y-%W', event_timestamp) AS week,

COUNT(DISTINCT user_id) AS wau

FROM events

GROUP BY week

ORDER BY week;
"""


# ----------------------------------------------------
# Monthly Active Users
# ----------------------------------------------------

MAU_QUERY = """
SELECT

strftime('%Y-%m', event_timestamp) AS month,

COUNT(DISTINCT user_id) AS mau

FROM events

GROUP BY month

ORDER BY month;
"""


# ----------------------------------------------------
# New Users
# ----------------------------------------------------

NEW_USERS_QUERY = """
SELECT

DATE(signup_date) AS signup_day,

COUNT(*) AS new_users

FROM users

GROUP BY signup_day

ORDER BY signup_day;
"""


# ----------------------------------------------------
# Feature Adoption
# ----------------------------------------------------

FEATURE_ADOPTION_QUERY = """
SELECT

feature_name,

COUNT(*) AS total_events

FROM events

GROUP BY feature_name

ORDER BY total_events DESC;
"""