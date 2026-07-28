from app.ai.ollama_client import ask_llm


def summarize(question, dataframe):

    prompt = f"""
You are a Senior Product Analyst.

A stakeholder asked:

{question}

Here is the query result:

{dataframe.to_markdown(index=False)}

Write a concise executive summary.

Rules:

- Maximum 4 bullet points.
- Mention the most important insights.
- Mention trends if visible.
- Mention anomalies if visible.
- Do NOT invent numbers.
- Use professional business language.
"""

    return ask_llm(prompt)