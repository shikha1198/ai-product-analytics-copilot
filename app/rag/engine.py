from app.rag.loader import load_documents
from app.rag.chunker import chunk_documents
from app.rag.retriever import Retriever
from app.rag.qa import answer_question

retriever = None


def get_retriever():
    global retriever

    if retriever is None:

        retriever = Retriever()

        documents = load_documents()
        chunks = chunk_documents(documents)

        retriever.build(chunks)

    return retriever


def ask_documents(question):

    retriever = get_retriever()

    relevant_chunks = retriever.search(
        question,
        k=3,
    )

    return answer_question(
        question,
        relevant_chunks,
    )