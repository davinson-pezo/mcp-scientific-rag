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

Este proyecto es una evolución de alto rendimiento de [mcp-rag-local](https://github.com/renl/mcp-rag-local). Hemos rediseñado la arquitectura original para cubrir las necesidades específicas de la **comunidad científica**, donde la precisión en PDFs complejos y la privacidad local son innegociables.

### 🔬 Mejoras Clave para Ciencia

1. **Extracción Avanzada (`pymupdf4llm`)**:
   - A diferencia de los extractores estándar, `pymupdf4llm` convierte tablas, fórmulas y estructuras de documentos científicos directamente en **Markdown limpio**, ideal para que el LLM lo entienda sin errores.
2. **Embeddings de Alta Calidad (`nomic-embed-text`)**:
   - Integración nativa con **Ollama**. Este modelo supera a los modelos ligeros tradicionales, ofreciendo una ventana de contexto mucho mayor y una comprensión semántica superior para términos técnicos densos.
3. **Base de Datos JSON Portable**:
   - Hemos eliminado la dependencia pesada de ChromaDB/Docker. Usamos un sistema de vectores basado en JSON nativo de Python: **ligero, rápido y sin configuraciones complejas**, ideal para investigadores que necesitan portabilidad.
4. **Procesamiento por Lotes**:
   - Soporte nativo para indexar hasta 10 artículos científicos simultáneamente con fragmentación (chunking) optimizada de 1500 caracteres.

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
git clone https://github.com/your-username/mcp-scientific-rag.git
cd mcp-scientific-rag

# Sync dependencies
uv sync
```

### 4. Configure your AI Client

Add this to your MCP configuration (e.g., Claude Desktop, Cursor, or Antigravity settings):

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

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
