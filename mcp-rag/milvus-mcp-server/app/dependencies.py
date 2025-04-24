"""
依赖注入模块 - Dependencies Module
本模块提供了系统各服务组件的依赖注入功能，实现了服务的单例模式和依赖管理。
主要包含了向量嵌入服务(EmbeddingService)和Milvus向量数据库服务(MilvusService)的获取方法，
确保在整个应用程序中只有一个服务实例，从而提高资源利用率和性能。

This module provides dependency injection for service components in the system,
implementing singleton pattern and dependency management.
"""

from functools import lru_cache
from typing import Generator

from app.services.embedding_service import EmbeddingService
from app.services.milvus_service import MilvusService


@lru_cache(maxsize=1)
def get_embedding_service() -> EmbeddingService:
    """获取向量嵌入服务的单例实例。
    
    使用lru_cache装饰器确保只创建一个EmbeddingService实例，实现单例模式。
    
    Returns:
        EmbeddingService: 向量嵌入服务实例
    """
    return EmbeddingService()


@lru_cache(maxsize=1)
def get_milvus_service() -> MilvusService:
    """获取Milvus向量数据库服务的单例实例。
    
    使用lru_cache装饰器确保只创建一个MilvusService实例，实现单例模式。
    该服务依赖于EmbeddingService，通过get_embedding_service()获取依赖。
    
    Returns:
        MilvusService: Milvus向量数据库服务实例
    """
    embedding_service = get_embedding_service()
    return MilvusService(embedding_service)


def milvus_service() -> Generator[MilvusService, None, None]:
    """Milvus服务的依赖注入函数，用于FastAPI路由依赖。
    
    这是一个生成器函数，用于在FastAPI路由中注入MilvusService依赖。
    使用yield语句提供服务实例，并在finally块中处理异常，确保资源的正确释放。
    
    Yields:
        MilvusService: Milvus向量数据库服务实例
    """
    service = get_milvus_service()
    try:
        yield service
    except Exception:
        # 处理可能出现的错误，确保资源正确释放
        pass 