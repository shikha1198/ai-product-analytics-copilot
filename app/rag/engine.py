from app.rag.loader import load_documents
from app.rag.chunker import chunk_documents
from app.rag.retriever import Retriever
from app.rag.qa import answer_question

retriever = Retriever()

documents = load_documents()
chunks = chunk_documents(documents)

retriever.build(chunks)


def ask_documents(question):

    relevant_chunks = retriever.search(
        question,
        k=3,
    )

    answer = answer_question(
        question,
        relevant_chunks,
    )

    return answer