import ollama

MODEL = "qwen2.5:7b"


def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to the local Ollama model
    and returns only the generated text.
    """

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]