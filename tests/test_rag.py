from app.rag.loader import load_documents
from app.rag.chunker import chunk_documents
from app.rag.retriever import Retriever
from app.rag.qa import answer_question

docs = load_documents()

chunks = chunk_documents(docs)

retriever = Retriever()
retriever.build(chunks)

question = "What does this document teach?"

relevant_chunks = retriever.search(
    question,
    k=3,
)

answer = answer_question(
    question,
    relevant_chunks,
)

print("\nQuestion:")
print(question)

print("\nAnswer:\n")
print(answer)