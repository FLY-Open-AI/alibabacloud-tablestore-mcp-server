# Milvus MCP Server

A Python implementation of MCP (Model Context Protocol) Server with Milvus as the vector database backend.

> [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open protocol supporting seamless integration between large language model (LLM) applications and external data sources and tools.
> Whether you're developing AI-driven integrated development environments (IDEs), enhancing chat interface capabilities, or creating custom AI workflows, MCP provides a standardized solution for efficiently connecting LLMs with the critical contextual information they need.

This Python implementation of MCP Server provides the same API as the original tablestore-mcp-server, but uses Milvus as the vector database backend.

## Prerequisites

1. Python 3.9+
2. Milvus database (can be running locally with Docker or as a cloud service)

## Setup and Running

### Environment Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd milvus-mcp-server
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Configuration

The application uses environment variables for configuration. Create a `.env` file in the root directory with the following variables:

```
MILVUS_HOST=localhost
MILVUS_PORT=19530
EMBEDDING_MODEL=all-MiniLM-L6-v2
KNOWLEDGE_COLLECTION=knowledge_store
FAQ_COLLECTION=faq_store
VECTOR_DIMENSION=384
```

Alternatively, you can set these environment variables directly:

```bash
export MILVUS_HOST=localhost
export MILVUS_PORT=19530
export EMBEDDING_MODEL=all-MiniLM-L6-v2
export KNOWLEDGE_COLLECTION=knowledge_store
export FAQ_COLLECTION=faq_store
export VECTOR_DIMENSION=384
```

### Running the Server

Start the server with:

```bash
cd milvus-mcp-server
python -m app.main
```

The server will be available at http://localhost:8000

## API Endpoints

The server exposes the following MCP API endpoints:

- `POST /api/v1/storeKnowledge`: Store document into knowledge store
- `POST /api/v1/searchKnowledge`: Search for similar documents in the knowledge store
- `POST /api/v1/storeFAQ`: Store FAQ content 
- `POST /api/v1/searchFAQ`: Search for similar FAQ content

## Tools Provided

The following tools are available for MCP clients:

1. `storeKnowledge`: Store document into knowledge store for later retrieval
2. `searchKnowledge`: Search for similar documents in the knowledge store
3. `storeFAQ`: Store document into FAQ store for later retrieval
4. `searchFAQ`: Search for similar documents in the FAQ store

## Using with MCP Clients

This server is compatible with any MCP client. To use it, point your MCP client to the server URL. 