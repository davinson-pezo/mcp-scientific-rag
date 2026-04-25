# 🧬 MCP Scientific RAG (Local Server)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Supported-orange.svg)](https://modelcontextprotocol.io/)

A high-performance, 100% private, and local Retrieval-Augmented Generation (RAG) system engineered specifically for **scientific research**. Built on the Model Context Protocol (MCP), it transforms your local machine into a centralized AI knowledge base, enabling assistants like Claude or Cursor to instantly search, extract, and synthesize insights from dense technical PDFs, tables, and complex scientific notation.

---

## 🔬 Why Scientists Need a Specialized RAG

Researchers today are drowning in literature, but standard AI tools and generic RAG implementations fundamentally fail in scientific workflows:

1. **The PDF Parsing Nightmare**: Scientific papers use complex multi-column layouts, intricate tables, and heavy mathematical formulas. Standard extractors turn these into unreadable gibberish.
2. **Strict Data Privacy**: Researchers constantly handle sensitive patient data, unpublished manuscripts, or proprietary chemical formulas. Uploading these to third-party APIs (like OpenAI or Anthropic clouds) is a massive security risk or outright policy violation.
3. **High Context Density**: Generic embedding models cannot distinguish between highly nuanced technical jargon, leading to poor semantic search results and AI hallucinations.
4. **Scattered Knowledge**: Literature is usually scattered across dozens of project folders, making it impossible to "connect the dots" across different disciplines over time.

**MCP Scientific RAG** solves this by providing a specialized, fully local infrastructure. It uses state-of-the-art layout-aware extractors (`pymupdf4llm`) and high-dimensional embeddings (`nomic-embed-text` via Ollama) to give your AI assistant flawless, secure, and permanent memory of your research.

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

## 🧠 Architecture: The Centralized Brain

Unlike traditional RAG systems that require maintaining a separate vector database for every project folder, this MCP server acts as a **single, global knowledge base** for your entire machine. 

You can ask your LLM to index PDFs scattered across your computer (Downloads, Research folders, etc.), and the server will centralize all extracted text and embeddings into a single `~/.mcp/scientific-rag/simple_db.json` file. This allows your AI to cross-reference concepts from a paper you read in January with a completely different project you are working on in April.

```text
+----------------------+        1. Finds PDFs       +----------------------+
|   Scattered PDFs     | -------------------------> |    AI Assistant      |
| (Project A, Dwnlds)  |                            | (Claude/Cursor/etc)  |
+----------------------+                            +---------+------------+
                                                              |
                                 2. Calls index_multiple_pdfs |
                                      or search_knowledge     |
                                                              v
+----------------------+        3. Gets Vectors     +----------------------+
|        Ollama        | <------------------------> |   MCP RAG Server     |
|  (nomic-embed-text)  |                            |  (pymupdf4llm)       |
+----------------------+                            +---------+------------+
                                                              |
                                        4. Stores / Retrieves |
                                                              v
                                                    +----------------------+
                                                    | Centralized Database |
                                                    |  (simple_db.json)    |
                                                    +----------------------+
```

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
| `memorize_multiple_texts`| Memorize a list of text snippets or research notes in a single batch operation. |

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

[![PayPal](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/donate?business=davinson@gmail.com&no_recurring=0&item_name=Scientific+RAG+Support&currency_code=EUR)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
