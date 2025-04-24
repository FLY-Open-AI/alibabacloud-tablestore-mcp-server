import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from loguru import logger

from app.api import mcp
from app.dependencies import milvus_service
from app.services.milvus_service import MilvusService
from app.utils.logging import get_logger

# Configure logging
logger = get_logger()

# Create FastAPI app
app = FastAPI(
    title="Milvus MCP Server",
    description="A Python implementation of MCP Server with Milvus as the vector database backend",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include API routers
app.include_router(mcp.router)

# Override dependency
app.dependency_overrides[MilvusService] = milvus_service


@app.get("/")
async def root():
    """Root endpoint.
    
    Returns:
        Welcome message
    """
    return {"message": "Welcome to Milvus MCP Server", "docs": "/docs"}


@app.get("/health")
async def health_check():
    """Health check endpoint.
    
    Returns:
        Health status
    """
    return {"status": "healthy"}


if __name__ == "__main__":
    # Get server port from environment variable or use default
    port = int(os.getenv("PORT", "8000"))
    
    # Start server
    logger.info(f"Starting Milvus MCP Server on port {port}")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True) 