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

## 中文文档

# Milvus MCP 服务器

基于 Milvus 向量数据库的 MCP（模型上下文协议）服务器的 Python 实现。

> [模型上下文协议 (MCP)](https://modelcontextprotocol.io/introduction) 是一个开放协议，支持大型语言模型 (LLM) 应用程序与外部数据源和工具的无缝集成。
> 无论您是开发 AI 驱动的集成开发环境 (IDE)，增强聊天界面功能，还是创建自定义 AI 工作流，MCP 都为有效连接 LLM 与其所需的关键上下文信息提供了标准化解决方案。

这个 MCP 服务器的 Python 实现提供了与原始 tablestore-mcp-server 相同的 API，但使用 Milvus 作为向量数据库后端。

## 前提条件

1. Python 3.9+
2. Milvus 数据库（可以通过 Docker 在本地运行或作为云服务使用）

## 设置和运行

### 环境设置

1. 克隆仓库：
```bash
git clone <仓库-URL>
cd milvus-mcp-server
```

2. 创建虚拟环境（可选但推荐）：
```bash
python -m venv venv
source venv/bin/activate  # 在 Windows 上: venv\Scripts\activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

### 配置

应用程序使用环境变量进行配置。在根目录中创建一个 `.env` 文件，包含以下变量：

```
MILVUS_HOST=localhost
MILVUS_PORT=19530
EMBEDDING_MODEL=all-MiniLM-L6-v2
KNOWLEDGE_COLLECTION=knowledge_store
FAQ_COLLECTION=faq_store
VECTOR_DIMENSION=384
```

或者，您可以直接设置这些环境变量：

```bash
export MILVUS_HOST=localhost
export MILVUS_PORT=19530
export EMBEDDING_MODEL=all-MiniLM-L6-v2
export KNOWLEDGE_COLLECTION=knowledge_store
export FAQ_COLLECTION=faq_store
export VECTOR_DIMENSION=384
```

### 运行服务器

通过以下命令启动服务器：

```bash
cd milvus-mcp-server
python -m app.main
```

服务器将在 http://localhost:8000 上可用

## API 端点

服务器提供以下 MCP API 端点：

- `POST /api/v1/storeKnowledge`: 将文档存储到知识库
- `POST /api/v1/searchKnowledge`: 在知识库中搜索相似文档
- `POST /api/v1/storeFAQ`: 存储常见问题解答内容
- `POST /api/v1/searchFAQ`: 搜索相似的常见问题解答内容

## 提供的工具

以下工具可供 MCP 客户端使用：

1. `storeKnowledge`: 将文档存储到知识库中以便日后检索
2. `searchKnowledge`: 在知识库中搜索相似文档
3. `storeFAQ`: 将文档存储到常见问题解答库中以便日后检索
4. `searchFAQ`: 在常见问题解答库中搜索相似文档

## 与 MCP 客户端一起使用

该服务器与任何 MCP 客户端兼容。要使用它，请将您的 MCP 客户端指向服务器 URL。 