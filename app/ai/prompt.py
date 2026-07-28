SCHEMA = """
Database Schema

Table: users

- user_id
- name
- email
- signup_date
- country
- device_type
- plan
- persona

Table: events

- event_id
- user_id
- session_id
- event_name
- event_timestamp
- feature_name
- device_type
- country
- event_properties
"""

EXAMPLES = """
Question:
Show DAU trend

SQL:
SELECT
DATE(event_timestamp) AS activity_date,
COUNT(DISTINCT user_id) AS dau
FROM events
GROUP BY DATE(event_timestamp)
ORDER BY activity_date;

----------------------------------------

Question:
Show WAU

SQL:
SELECT
strftime('%Y-%W', event_timestamp) AS week,
COUNT(DISTINCT user_id) AS wau
FROM events
GROUP BY week
ORDER BY week;

----------------------------------------

Question:
Show MAU

SQL:
SELECT
strftime('%Y-%m', event_timestamp) AS month,
COUNT(DISTINCT user_id) AS mau
FROM events
GROUP BY month
ORDER BY month;

----------------------------------------

Question:
Top countries by active users

SQL:
SELECT
users.country,
COUNT(DISTINCT events.user_id) AS active_users
FROM events
JOIN users
ON users.user_id = events.user_id
GROUP BY users.country
ORDER BY active_users DESC
LIMIT 10;

----------------------------------------

Question:
Feature adoption

SQL:
SELECT
feature_name,
COUNT(*) AS total_events
FROM events
GROUP BY feature_name
ORDER BY total_events DESC;

----------------------------------------

Question:
Daily signups

SQL:
SELECT
signup_date,
COUNT(*) AS new_users
FROM users
GROUP BY signup_date
ORDER BY signup_date;
"""

def build_prompt(question: str):

    return f"""
You are an expert Product Analytics SQL assistant.

Generate ONLY valid SQLite SQL.

Rules:

- Return ONLY SQL.
- No explanation.
- No markdown.
- No ```sql blocks.
- Use SQLite syntax only.
- Use table-qualified column names when joining tables.
- Never use SELECT *.
- Always give meaningful aliases.
- Prefer COUNT(DISTINCT user_id) for user metrics.
- If two tables share a column (country, device_type, user_id), ALWAYS prefix with the table name.

{SCHEMA}

Examples:

{EXAMPLES}

User Question:

{question}

SQL:
"""