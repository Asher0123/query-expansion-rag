import numpy as np

from src.main import Retriever
from src.loaders import Document


class MockLoader:

    def load_document(self, path):

        return [
            Document(
                content=(
                    "AWS provides cloud computing."
                ),
                metadata={}
            )
        ]


class MockSplitter:

    def split(self, documents):

        return documents


class MockEmbedder:

    def get_embeddings(self, texts):

        return np.array(
            [[0.1, 0.2, 0.3]],
            dtype=np.float32
        )


def test_ingestion():

    retriever = Retriever(
        loader=MockLoader(),
        splitter=MockSplitter(),
        embedder=MockEmbedder()
    )

    index = retriever.ingest("dummy.pdf")

    assert index.ntotal == 1