from app.rag.loader import load_documents
from app.rag.chunker import chunk_documents

docs = load_documents()

chunks = chunk_documents(docs)

print(f"Documents: {len(docs)}")
print(f"Chunks: {len(chunks)}")

print()

print(chunks[0]["text"])