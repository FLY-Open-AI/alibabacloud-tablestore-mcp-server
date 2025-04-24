from fastapi import APIRouter, Depends
from typing import List
from pydantic import json_schema

from app.models.models import (
    KnowledgeContent, 
    SearchKnowledgeQuery, 
    FAQContent, 
    SearchFAQQuery,
    MCPTools,
    MCPTool
)
from app.services.milvus_service import MilvusService

router = APIRouter(prefix="/api/v1")


def get_tools() -> MCPTools:
    """Get the available MCP tools.
    
    Returns:
        The tools response object
    """
    tools = [
        MCPTool(
            name="storeKnowledge",
            description="Store document into knowledge store for later retrieval.",
            input_schema=json_schema.model_json_schema(KnowledgeContent)
        ),
        MCPTool(
            name="searchKnowledge",
            description="Search for similar documents on natural language descriptions from knowledge store.",
            input_schema=json_schema.model_json_schema(SearchKnowledgeQuery)
        ),
        MCPTool(
            name="storeFAQ",
            description="Store document into FAQ store for later retrieval.",
            input_schema=json_schema.model_json_schema(FAQContent)
        ),
        MCPTool(
            name="searchFAQ",
            description="Search for similar documents on natural language descriptions from FAQ store.",
            input_schema=json_schema.model_json_schema(SearchFAQQuery)
        )
    ]
    return MCPTools(tools=tools)


@router.get("/tools")
async def tools() -> MCPTools:
    """Get the available MCP tools.
    
    Returns:
        The tools response
    """
    return get_tools()


@router.post("/storeKnowledge", status_code=201)
async def store_knowledge(
    content: KnowledgeContent,
    milvus_service: MilvusService = Depends()
) -> None:
    """Store a document in the knowledge store.
    
    Args:
        content: The knowledge content to store
        milvus_service: The Milvus service
    """
    milvus_service.store_knowledge(content)


@router.post("/searchKnowledge")
async def search_knowledge(
    query: SearchKnowledgeQuery,
    milvus_service: MilvusService = Depends()
) -> List[KnowledgeContent]:
    """Search for documents in the knowledge store.
    
    Args:
        query: The search query
        milvus_service: The Milvus service
        
    Returns:
        List of matching documents
    """
    return milvus_service.search_knowledge(query.query, query.size)


@router.post("/storeFAQ", status_code=201)
async def store_faq(
    content: FAQContent,
    milvus_service: MilvusService = Depends()
) -> None:
    """Store an FAQ in the FAQ store.
    
    Args:
        content: The FAQ content to store
        milvus_service: The Milvus service
    """
    milvus_service.store_faq(content)


@router.post("/searchFAQ")
async def search_faq(
    query: SearchFAQQuery,
    milvus_service: MilvusService = Depends()
) -> List[FAQContent]:
    """Search for FAQs in the FAQ store.
    
    Args:
        query: The search query
        milvus_service: The Milvus service
        
    Returns:
        List of matching FAQs
    """
    return milvus_service.search_faq(query.query, query.size) 