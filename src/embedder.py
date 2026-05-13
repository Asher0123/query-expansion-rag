from fastembed import TextEmbedding
from typing import Optional,List, Any
import numpy as np
# from loaders import Document
from exceptions import EmbeddingError

class MockTextEmbeddingModel:
    """
    Wrapper around embedding models.

    Provides a common interface for generating vector embeddings
    from text using any supported embedding backend.
    """
    def __init__(self, model=TextEmbedding(),method_name='embed'):
        """
        Initialize the embedding model wrapper.

        Args:
            model:
                Embedding model instance to use for generating embeddings.

            method_name:
                Name of the embedding method exposed by the model.
                Default is 'embed'.
        """
        self.model=model
        self.method_name=method_name
    
    def get_embeddings(self, chunks: List[str]) -> np.ndarray:
        """
        Generate vector embeddings for input text chunks.

        Args:
            chunks:
                List of text chunks to embed.

        Returns:
            NumPy array containing vector embeddings for each chunk.
        """
        try:
            if not chunks:
                raise EmbeddingError(
                    "No chunks provided for embedding"
                )
            
            if not any(chunk.strip() for chunk in chunks):
                raise EmbeddingError(f"Provided chunks contain no valid text")
            
            if not hasattr(self.model, self.method_name):
                raise EmbeddingError(
                    f"{self.model.__class__.__name__} "
                    f"does not implement '{self.method_name}'"
                )

            embeddings = getattr(self.model, self.method_name)(chunks)

            embeddings = np.array(list(embeddings), dtype="float32")
            
            if embeddings.size == 0:
                raise EmbeddingError(
                    "Generated embeddings are empty"
                )

            return embeddings

        except EmbeddingError:
            raise

        except Exception as e:
            raise EmbeddingError(
                f"Failed to generate embeddings using {self.model.__class__.__name__} due to error {e}" 
            ) from e
