CHUNK_SIZE = 500
OVERLAP = 100


def chunk_documents(documents):

    chunks = []

    for doc in documents:

        text = doc["text"]

        start = 0

        while start < len(text):

            chunk = text[start:start + CHUNK_SIZE]

            chunks.append(
                {
                    "filename": doc["filename"],
                    "text": chunk,
                }
            )

            start += CHUNK_SIZE - OVERLAP

    return chunks