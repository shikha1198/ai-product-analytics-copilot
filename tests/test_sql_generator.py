from app.ai.sql_generator import generate_sql

question = "Show top 10 countries by active users"

sql = generate_sql(question)

print(sql)