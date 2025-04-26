import os
from loguru import logger
import uvicorn
from app.utils.logging import get_logger
from app.mcp_server import MilvusMCPServer

# Configure logging
logger = get_logger()

# Create MCP server instance
mcp_server = MilvusMCPServer()

if __name__ == "__main__":
    # Get server port from environment variable or use default
    port = int(os.getenv("PORT", "8080"))
    
    # Start server
    logger.info(f"Starting Milvus MCP Server on port {port}")
    mcp_server.run(host="0.0.0.0", port=port) 