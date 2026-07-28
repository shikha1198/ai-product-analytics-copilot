import faiss
import numpy as np

from app.rag.embeddings import get_model


class Retriever:

    def __init__(self):
        self.index = None
        self.chunks = None

    def build(self, chunks):

        self.chunks = chunks

        model = get_model()

        embeddings = model.encode(
            [chunk["text"] for chunk in chunks],
            convert_to_numpy=True,
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            embeddings.astype(np.float32)
        )

    def search(self, question, k=3):

        model = get_model()

        query_embedding = model.encode(
            [question],
            convert_to_numpy=True,
        )

        distances, indices = self.index.search(
            query_embedding.astype(np.float32),
            k,
        )

        return [
            self.chunks[i]
            for i in indices[0]
        ]