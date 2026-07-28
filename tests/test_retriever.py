from app.rag.loader import load_documents
from app.rag.chunker import chunk_documents
from app.rag.retriever import Retriever

docs = load_documents()

chunks = chunk_documents(docs)

retriever = Retriever()

retriever.build(chunks)

results = retriever.search(
    "What does this document teach?"
)

print()

for i, chunk in enumerate(results):

    print("=" * 80)

    print(f"Chunk {i+1}")

    print()

    print(chunk["text"][:500])