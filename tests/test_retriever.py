import json
import numpy as np

from src.main import Retriever
from src.loaders import Document


class MockLoader:

    def load_document(self, path):

        return [
            Document(
                content=(
                    "AWS provides scalable cloud computing."
                ),
                metadata={
                    "source": "mock.pdf",
                    "page_no": 1
                }
            ),

            Document(
                content=(
                    "Amazon VPC enables isolated networking."
                ),
                metadata={
                    "source": "mock.pdf",
                    "page_no": 2
                }
            )
        ]


class MockSplitter:

    def split(self, documents):

        return documents


class MockEmbedder:

    def get_embeddings(self, texts):

        return np.array(
            [
                [0.1, 0.2, 0.3],
                [0.2, 0.1, 0.4]
            ],
            dtype=np.float32
        )


def setup_retriever():

    retriever = Retriever(
        loader=MockLoader(),
        splitter=MockSplitter(),
        embedder=MockEmbedder()
    )

    retriever.ingest("dummy.pdf")

    return retriever


def test_query_returns_results():

    retriever = setup_retriever()

    results = retriever.query(
        "What is AWS?"
    )

    assert len(results) > 0


def test_result_structure():

    retriever = setup_retriever()

    results = retriever.query(
        "What is AWS?"
    )

    result = results[0]

    assert "page_content" in result
    assert "metadata" in result
    assert "cosine similarity" in result


def test_cosine_similarity_range():

    retriever = setup_retriever()

    results = retriever.query(
        "What is AWS?"
    )

    similarity = results[0][
        "cosine similarity"
    ]

    assert 0 <= similarity <= 1


def test_top_k_retrieval():

    retriever = setup_retriever()

    results = retriever.query(
        "What is AWS?",
        k=2
    )

    assert len(results) == 2


def test_metadata_exists():

    retriever = setup_retriever()

    results = retriever.query(
        "What is AWS?"
    )

    metadata = results[0]["metadata"]

    assert "source" in metadata
    assert "page_no" in metadata