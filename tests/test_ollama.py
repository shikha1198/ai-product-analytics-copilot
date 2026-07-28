from app.ai.ollama_client import ask_llm

response = ask_llm(
    "Say hello in one sentence."
)

print(response)