from functools import lru_cache
from typing import Generator

from app.services.embedding_service import EmbeddingService
from app.services.milvus_service import MilvusService


@lru_cache(maxsize=1)
def get_embedding_service() -> EmbeddingService:
    """Get the embedding service singleton.
    
    Returns:
        The embedding service
    """
    return EmbeddingService()


@lru_cache(maxsize=1)
def get_milvus_service() -> MilvusService:
    """Get the Milvus service singleton.
    
    Returns:
        The Milvus service
    """
    embedding_service = get_embedding_service()
    return MilvusService(embedding_service)


def milvus_service() -> Generator[MilvusService, None, None]:
    """Dependency for the Milvus service.
    
    Yields:
        The Milvus service instance
    """
    service = get_milvus_service()
    try:
        yield service
    except Exception:
        # Handle any errors
        pass 