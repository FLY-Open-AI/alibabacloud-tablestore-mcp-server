from mcp.server import FastMCP
from typing import Any, Dict, List
from loguru import logger
from app.services.milvus_service import MilvusService
from app.models.models import KnowledgeContent, FAQContent
from app.dependencies import get_milvus_service_dependency

class MilvusMCPServer(FastMCP):
    """MCP server implementation for Milvus vector database."""
    
    def __init__(self):
        super().__init__()
        self.milvus_service = get_milvus_service_dependency()
        
        # Register tools
        self.register_tool(
            "storeKnowledge",
            self.store_knowledge,
            "Store document into knowledge store for later retrieval.",
            {
                "type": "object",
                "properties": {
                    "content": {"type": "string", "description": "The knowledge content to store"},
                    "metadata": {
                        "type": "object",
                        "description": "Additional metadata for the knowledge content",
                        "additionalProperties": True
                    }
                },
                "required": ["content"]
            }
        )
        
        self.register_tool(
            "searchKnowledge",
            self.search_knowledge,
            "Search for similar documents on natural language descriptions from knowledge store.",
            {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"},
                    "size": {"type": "integer", "description": "Number of results to return", "default": 5}
                },
                "required": ["query"]
            }
        )
        
        self.register_tool(
            "storeFAQ",
            self.store_faq,
            "Store document into FAQ store for later retrieval.",
            {
                "type": "object",
                "properties": {
                    "question": {"type": "string", "description": "The FAQ question"},
                    "answer": {"type": "string", "description": "The FAQ answer"},
                    "metadata": {
                        "type": "object",
                        "description": "Additional metadata for the FAQ",
                        "additionalProperties": True
                    }
                },
                "required": ["question", "answer"]
            }
        )
        
        self.register_tool(
            "searchFAQ",
            self.search_faq,
            "Search for similar documents on natural language descriptions from FAQ store.",
            {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"},
                    "size": {"type": "integer", "description": "Number of results to return", "default": 5}
                },
                "required": ["query"]
            }
        )
        
    async def store_knowledge(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Store knowledge content in Milvus."""
        try:
            content = KnowledgeContent(
                content=args["content"],
                metadata=args.get("metadata", {})
            )
            await self.milvus_service.store_knowledge(content)
            return {"status": "success", "message": "Knowledge stored successfully"}
        except Exception as e:
            logger.error(f"Error storing knowledge: {e}")
            return {"status": "error", "message": str(e)}
            
    async def search_knowledge(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Search knowledge content in Milvus."""
        try:
            size = args.get("size", 5)
            results = await self.milvus_service.search_knowledge(args["query"], size)
            return {
                "status": "success",
                "results": [result.dict() for result in results]
            }
        except Exception as e:
            logger.error(f"Error searching knowledge: {e}")
            return {"status": "error", "message": str(e)}
            
    async def store_faq(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Store FAQ content in Milvus."""
        try:
            content = FAQContent(
                question=args["question"],
                answer=args["answer"],
                metadata=args.get("metadata", {})
            )
            await self.milvus_service.store_faq(content)
            return {"status": "success", "message": "FAQ stored successfully"}
        except Exception as e:
            logger.error(f"Error storing FAQ: {e}")
            return {"status": "error", "message": str(e)}
            
    async def search_faq(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Search FAQ content in Milvus."""
        try:
            size = args.get("size", 5)
            results = await self.milvus_service.search_faq(args["query"], size)
            return {
                "status": "success",
                "results": [result.dict() for result in results]
            }
        except Exception as e:
            logger.error(f"Error searching FAQ: {e}")
            return {"status": "error", "message": str(e)} 