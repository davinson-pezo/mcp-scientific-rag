# Scientific RAG Server (mcp-rag-local)

This is a highly customized Model Context Protocol (MCP) server tailored for processing scientific research. It provides a lightweight, optimized Retrieval-Augmented Generation (RAG) system running entirely locally.

## 🚀 Key Architectural Upgrades

1. **State-of-the-Art PDF Extraction (`pymupdf4llm`)**:
   - Upgraded from standard text parsers to `pymupdf4llm`. This library natively converts complex PDF elements (scientific paragraphs, tables, and structures) directly into clean Markdown, which is optimized specifically for LLM ingestion.
2. **Advanced Embedding Model**:
   - Now powered by **`nomic-embed-text`** via Ollama. It offers superior semantic understanding of dense scientific contexts and large context lengths compared to standard mini-LM models.
3. **Lightweight Portable Database**:
   - Removed the heavy ChromaDB Docker dependency. The system now uses a highly portable, lightweight JSON vector database (`simple_db.json`) powered by native cosine similarity search in Python. This allows easy syncing and sharing across devices without complex database administration.
4. **Batch Processing**:
   - Implemented an `index_multiple_pdfs` tool to process up to 10 scientific papers at a time with automatic and seamless chunking (1500 characters per chunk).

## 📄 Supported Documents

- **PDF Documents (.pdf)**: It directly extracts, formats into markdown, chunks, and vectorizes local PDF files.
- **Raw Text Strings**: Arbitrary text snippets, notes, or web extracts can be manually loaded via basic memory tools.

## 🛠️ MCP Tools Available

The server exposes the following tools to the AI:
- `index_multiple_pdfs(file_paths)`: Processes and indexes up to 10 local PDF files in parallel.
- `search_knowledge(query, n_results)`: Performs mathematical vector similarity search in the JSON database to return the most relevant document chunks.
- `list_indexed_files()`: Returns a list of all PDFs currently loaded in the AI's memory.
- `clear_knowledge_base()`: Wipes the entire local database.
- `memorize_text(text, metadata)` & `memorize_multiple_texts(texts)`: Store free-form texts directly into the memory vectors.

---

## ⚙️ Setup Instructions

### 1. Install Dependencies
You need [uv](https://github.com/astral-sh/uv) installed to run the server.
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Prepare the AI Model
Ensure you have [Ollama](https://ollama.com/) installed and running on your system. 
You must pull the custom embedding model:
```bash
ollama pull nomic-embed-text
```

### 3. Add to MCP Client (Claude / Cline / Antigravity)
Add the following configuration to your MCP settings file:
```json
"mcp-rag-local": {
  "command": "uv",
  "args": [
    "--directory",
    "/PATH/TO/YOUR/mcp-rag-local",
    "run",
    "main.py"
  ]
}
```
*(Make sure to update the path to point to your cloned repository folder).*
