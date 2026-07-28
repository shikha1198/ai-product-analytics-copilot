from app.ai.sql_generator import generate_sql
from app.ai.sql_executor import execute_sql

question = "Show top 10 countries by active users"

sql = generate_sql(question)

print("Generated SQL:")
print(sql)

print("\nExecuting...\n")

df = execute_sql(sql)

print(df)