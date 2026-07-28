from app.ai.ollama_client import ask_llm


def answer_question(question, chunks):

    context = "\n\n".join(
        chunk["text"] for chunk in chunks
    )

    prompt = f"""
You are a Product Analytics AI Assistant.

Answer ONLY using the context below.

If the answer is not present in the context, reply:

"I couldn't find that information in the uploaded documents."

Context:

{context}

Question:

{question}

Answer:
"""

    return ask_llm(prompt)