from app.rag.loader import load_documents

docs = load_documents()

print(f"Loaded {len(docs)} documents\n")

for doc in docs:
    print(doc["filename"])
    print(doc["text"][:500])
    print("-" * 50)