from sentence_transformers import SentenceTransformer

from src.embedder import MockTextEmbeddingModel


def test_embedding_creation():

    embedder = MockTextEmbeddingModel(
        model=SentenceTransformer(
            "all-MiniLM-L6-v2"
        ),
        method_name="encode"
    )

    embeddings = embedder.get_embeddings(
        ["Hello world"]
    )

    assert embeddings.shape[0] == 1


def test_embedding_dimension():

    embedder = MockTextEmbeddingModel(
        model=SentenceTransformer(
            "all-MiniLM-L6-v2"
        ),
        method_name="encode"
    )

    embeddings = embedder.get_embeddings(
        ["Hello world"]
    )

    assert embeddings.shape[1] > 0