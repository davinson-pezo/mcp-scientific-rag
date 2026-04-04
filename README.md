# 🧬 MCP Scientific RAG (Local Server)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Supported-orange.svg)](https://modelcontextprotocol.io/)

A high-performance, private, and local Retrieval-Augmented Generation (RAG) system specifically optimized for **scientific research**. Built on the Model Context Protocol (MCP), it enables AI agents to interact with dense technical PDFs, tables, and complex scientific notation with unprecedented accuracy.

---

## 🔬 The Problem: Standard RAG vs. Scientific Reality

Standard RAG implementations often fail in scientific workflows because:

- **Complex PDFs**: Traditional parsers struggle with multi-column layouts, tables, and mathematical formulas.
- **Privacy**: Researchers often deal with sensitive, unpublished data that cannot be sent to third-party clouds.
- **Context Density**: Scientific texts require higher-quality embeddings to distinguish between nuanced technical terms.

**MCP Scientific RAG** solves this by providing a specialized local infrastructure tailored for the scientific community.

---

## 🚀 Improvements & Origin

This project is a high-performance evolution of [mcp-rag-local](https://github.com/renl/mcp-rag-local). We have re-engineered the original architecture to address the specific needs of the **scientific community**, where precision in complex PDFs and local privacy are non-negotiable.

### 🔬 Core Scientific Enhancements

1. **State-of-the-Art Extraction (`pymupdf4llm`)**:
   - Unlike standard extractors, `pymupdf4llm` converts tables, formulas, and scientific document structures directly into **Clean Markdown**, making it ideal for LLMs to ingest technical data with zero transcription errors.
2. **High-Quality Embeddings (`nomic-embed-text`)**:
   - Native integration with **Ollama**. This model significantly outperforms traditional lightweight models, offering a much larger context window and superior semantic understanding for dense technical terms.
3. **Portable JSON Vector Database**:
   - We have removed the heavy dependency on ChromaDB/Docker. By using a native Python JSON vector system, the project remains **lightweight, fast, and zero-config**, perfect for researchers who need cross-platform portability.
4. **Enhanced Batch Processing**:
   - Native support for indexing up to 10 scientific papers simultaneously with optimized 1500-character chunking.

---

## 🛠️ MCP Tools Exposed

The server provides the following capabilities to your AI assistant:

| Tool | Description |
| :--- | :--- |
| `index_multiple_pdfs` | Intelligent extraction and vectorization of up to 10 local PDF files. |
| `search_knowledge` | High-precision vector similarity search across the scientific knowledge base. |
| `list_indexed_files` | Inventory of all documents currently in the local memory. |
| `clear_knowledge_base` | Securely wipes the local database. |
| `memorize_text` | Store arbitrary research notes, snippets, or findings directly into memory. |

---

## ⚙️ Quick Start

### 1. Requirements

- [Ollama](https://ollama.com/) (Running locally)
- [uv](https://astral.sh/uv) (Python package manager)

### 2. Prepare the Embedding Model

```bash
ollama pull nomic-embed-text
```

### 3. Installation

```bash
# Clone the repository
git clone https://github.com/davinson-pezo/mcp-scientific-rag.git
cd mcp-scientific-rag

# Sync dependencies
uv sync
```

### 4. Configure your AI Client

Add this to your MCP configuration (e.g., Claude Desktop, Cursor, VS Code, or Antigravity settings):

```json
"mcp-scientific-rag": {
  "command": "uv",
  "args": [
    "--directory",
    "/ABSOLUTE/PATH/TO/mcp-scientific-rag",
    "run",
    "main.py"
  ]
}
```

---

## 🛡️ Privacy & Security

- **100% Local**: No data leaves your machine. Embeddings and searches are processed locally via Ollama.
- **Sanitized Metadata**: The system is designed to avoid storing absolute local paths, ensuring your repository remains safe for public sharing.

---

## ☕ Support the Project

If this tool has been helpful to your research and you'd like to support its development, feel free to buy me a coffee!

[![PayPal](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/donate?business=davinson@gmail.com&no_recurring=0&item_name=Scientific+RAG+Support&currency_code=USD)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
