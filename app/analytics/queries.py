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

# ----------------------------------------------------
# Cohort Retention
# ----------------------------------------------------

COHORT_RETENTION_QUERY = """
WITH cohort_size AS (

    SELECT
        DATE(signup_date) AS cohort_date,
        COUNT(*) AS cohort_size
    FROM users
    GROUP BY DATE(signup_date)

),

daily_activity AS (

    SELECT DISTINCT

        u.user_id,

        DATE(u.signup_date) AS cohort_date,

        CAST(
            julianday(DATE(e.event_timestamp))
            -
            julianday(DATE(u.signup_date))
            AS INTEGER
        ) AS days_after_signup

    FROM users u

    JOIN events e
        ON u.user_id = e.user_id

    WHERE DATE(e.event_timestamp) >= DATE(u.signup_date)

)

SELECT

    d.cohort_date,

    d.days_after_signup,

    COUNT(DISTINCT d.user_id) AS active_users,

    c.cohort_size

FROM daily_activity d

JOIN cohort_size c
ON d.cohort_date = c.cohort_date

GROUP BY

    d.cohort_date,
    d.days_after_signup,
    c.cohort_size

ORDER BY

    d.cohort_date,
    d.days_after_signup;

"""

# ----------------------------------------------------
# Product Funnel
# ----------------------------------------------------

FUNNEL_QUERY = """
SELECT
    event_name,
    COUNT(DISTINCT user_id) AS users
FROM events
WHERE event_name IN (
    'signup',
    'login',
    'dashboard_viewed',
    'task_created',
    'task_completed'
)
GROUP BY event_name;
"""

# ----------------------------------------------------
# Daily Stickiness
# ----------------------------------------------------

STICKINESS_QUERY = """
WITH daily AS (

    SELECT

        DATE(event_timestamp) AS activity_date,

        COUNT(DISTINCT user_id) AS dau

    FROM events

    GROUP BY DATE(event_timestamp)

),

monthly AS (

    SELECT

        strftime('%Y-%m', event_timestamp) AS month,

        COUNT(DISTINCT user_id) AS mau

    FROM events

    GROUP BY month

)

SELECT

    d.activity_date,

    d.dau,

    m.mau,

    ROUND(
        d.dau * 100.0 / m.mau,
        2
    ) AS stickiness

FROM daily d

JOIN monthly m

ON strftime('%Y-%m', d.activity_date)=m.month

ORDER BY activity_date;
"""

# ----------------------------------------------------
# Growth Accounting
# ----------------------------------------------------

GROWTH_ACCOUNTING_QUERY = """
WITH daily_activity AS (

    SELECT DISTINCT

        user_id,

        DATE(event_timestamp) AS activity_date

    FROM events

),

previous_activity AS (

    SELECT

        user_id,

        activity_date,

        LAG(activity_date) OVER (

            PARTITION BY user_id

            ORDER BY activity_date

        ) AS previous_day

    FROM daily_activity

)

SELECT

    activity_date,

    SUM(
        CASE
            WHEN previous_day IS NULL
            THEN 1
            ELSE 0
        END
    ) AS new_users,

    SUM(
        CASE
            WHEN previous_day IS NOT NULL
            AND julianday(activity_date) - julianday(previous_day) = 1
            THEN 1
            ELSE 0
        END
    ) AS returning_users,

    SUM(
        CASE
            WHEN previous_day IS NOT NULL
            AND julianday(activity_date) - julianday(previous_day) > 1
            THEN 1
            ELSE 0
        END
    ) AS resurrected_users

FROM previous_activity

GROUP BY activity_date

ORDER BY activity_date;
"""