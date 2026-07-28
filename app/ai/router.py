from app.ai.intents import INTENTS
from app.rag.engine import ask_documents

from app.analytics.metrics import (
    calculate_dau,
    calculate_wau,
    calculate_mau,
    calculate_feature_adoption,
    calculate_funnel,
    calculate_stickiness,
    calculate_growth_accounting,
)

from app.ai.sql_generator import generate_sql
from app.ai.sql_executor import execute_sql


def route_question(question: str):

    question_lower = question.lower()

    for keyword in INTENTS["dau"]:
        if keyword in question_lower:
            return calculate_dau()

    for keyword in INTENTS["wau"]:
        if keyword in question_lower:
            return calculate_wau()

    for keyword in INTENTS["mau"]:
        if keyword in question_lower:
            return calculate_mau()

    for keyword in INTENTS["funnel"]:
        if keyword in question_lower:
            return calculate_funnel()

    for keyword in INTENTS["stickiness"]:
        if keyword in question_lower:
            return calculate_stickiness()

    for keyword in INTENTS["growth"]:
        if keyword in question_lower:
            return calculate_growth_accounting()

    for keyword in INTENTS["features"]:
        if keyword in question_lower:
            return calculate_feature_adoption()

    # AI SQL + RAG fallback
    try:

        sql = generate_sql(question)

        print("\nGenerated SQL:\n")
        print(sql)

        return execute_sql(sql)

    except Exception as e:

        print(f"\nSQL Generation Failed: {e}")
        print("Falling back to RAG...\n")

        return ask_documents(question)