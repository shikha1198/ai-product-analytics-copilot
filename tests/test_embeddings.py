from app.rag.loader import load_documents
from app.rag.chunker import chunk_documents
from app.rag.embeddings import create_embeddings

docs = load_documents()

chunks = chunk_documents(docs)

embeddings = create_embeddings(chunks)

print(f"Chunks: {len(chunks)}")
print(f"Embeddings shape: {embeddings.shape}")

print()
print(embeddings[0][:10])