import requests
import uuid
import os
import json
import math
from mcp.server.fastmcp import FastMCP, Context

# Configuración Global
OLLAMA_PORT = os.getenv("OLLAMA_PORT", "11434")
DB_FILE = os.path.expanduser("~/.mcp/scientific-rag/simple_db.json")
EMBEDDING_MODEL = "nomic-embed-text"

mcp = FastMCP("Scientific RAG Server")

def get_embedding(text: str):
    url = f"http://localhost:{OLLAMA_PORT}/api/embeddings"
    payload = {"model": EMBEDDING_MODEL, "prompt": text}
    try:
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        return response.json().get("embedding")
    except Exception:
        return None

def load_db():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    magnitude1 = math.sqrt(sum(a * a for a in v1))
    magnitude2 = math.sqrt(sum(b * b for b in v2))
    if magnitude1 == 0 or magnitude2 == 0: return 0
    return dot_product / (magnitude1 * magnitude2)

@mcp.tool()
def memorize_text(text: str, metadata: dict = {}) -> str:
    """Memoriza un fragmento de texto arbitrario en la base global."""
    vector = get_embedding(text)
    if not vector: return "Error: No se pudo generar embedding."
    db = load_db()
    db.append({
        "id": str(uuid.uuid4()),
        "vector": vector,
        "text": text,
        "source": "manual_entry",
        "page": 0,
        "metadata": metadata
    })
    save_db(db)
    return "Texto memorizado con éxito."

@mcp.tool()
def memorize_multiple_texts(texts: list) -> str:
    """Memoriza una lista de fragmentos de texto en una sola operación."""
    db = load_db()
    count = 0
    for text in texts:
        vector = get_embedding(text)
        if vector:
            db.append({
                "id": str(uuid.uuid4()),
                "vector": vector,
                "text": text,
                "source": "manual_batch",
                "page": 0
            })
            count += 1
    save_db(db)
    return f"Se han memorizado {count} textos."

@mcp.tool()
async def index_multiple_pdfs(ctx: Context, file_paths: list) -> str:
    """Indexa una lista de archivos PDF (Máx 10 por tanda)."""
    if len(file_paths) > 10:
        return "Error: Máximo 10 archivos por tanda."
    
    import pymupdf4llm
    
    results = []
    for path in file_paths:
        if not os.path.exists(path):
            results.append(f"No encontrado: {path}")
            continue
        try:
            text_content = pymupdf4llm.to_markdown(path)
            chunks = []
            chunk_size = 1500
            for i in range(0, len(text_content), chunk_size):
                chunks.append(text_content[i:i+chunk_size])
            db = load_db()
            for chunk in chunks:
                vector = get_embedding(chunk)
                if vector:
                    db.append({"id":str(uuid.uuid4()), "vector":vector, "text":chunk, "source":os.path.basename(path), "page":0})
            save_db(db)
            results.append(f"Indexado: {os.path.basename(path)}")
        except Exception as e:
            results.append(f"Error en {os.path.basename(path)}: {str(e)}")
    return "\n".join(results)

@mcp.tool()
def search_knowledge(query: str, n_results: int = 5) -> str:
    """Busca en la base de conocimientos científca global."""
    query_vector = get_embedding(query)
    if not query_vector: return "Error en Ollama."
    db = load_db()
    if not db: return "Base vacía."
    results = []
    for item in db:
        sim = cosine_similarity(query_vector, item["vector"])
        results.append((sim, item))
    results.sort(key=lambda x: x[0], reverse=True)
    top = results[:n_results]
    output = [f"Resultados para: '{query}'\n"]
    for i, (sim, item) in enumerate(top, 1):
        output.append(f"[{i}] [Sim: {sim:.4f}] {os.path.basename(item['source'])}:\n{item['text']}\n")
    return "\n".join(output)

@mcp.tool()
def list_indexed_files() -> str:
    """Lista todos los archivos únicos que han sido indexados en la base global."""
    db = load_db()
    files = sorted(list(set(item["source"] for item in db)))
    if not files: return "No hay archivos indexados."
    return "Archivos en la base de datos:\n" + "\n".join(f"- {f}" for f in files)

@mcp.tool()
def clear_knowledge_base() -> str:
    """BORRA todo el contenido de la base de datos global. Usar con precaución."""
    save_db([])
    return "Base de datos vaciada con éxito."

if __name__ == "__main__":
    mcp.run()
