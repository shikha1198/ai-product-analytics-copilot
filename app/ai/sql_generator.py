from app.ai.prompt import build_prompt
from app.ai.ollama_client import ask_llm


def generate_sql(question: str):

    prompt = build_prompt(question)

    sql = ask_llm(prompt)

    return sql.strip()