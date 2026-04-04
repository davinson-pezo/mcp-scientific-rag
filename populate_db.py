import os
import sys

# Import functions from main.py
sys.path.append(os.path.expanduser('~/.mcp/scientific-rag'))
from main import index_multiple_pdfs, search_knowledge
import asyncio

class MockContext:
    async def info(self, text):
        print(f"[INFO] {text}")
    async def error(self, text):
        print(f"[ERROR] {text}")

async def main():
    ctx = MockContext()
    # Define the path to your scientific papers (PDFs)
    # You can place them in a 'data' folder inside the project or use your own reference folder.
    data_dir = os.path.expanduser('~/Documents/references') # Update this path to your PDF folder
    
    if not os.path.exists(data_dir):
        print(f"[WARNING] Directory not found: {data_dir}")
        papers = []
    else:
        # Automatically find some PDFs in the directory for testing
        papers = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.pdf')][:5]
    print("Iniciando indexación...")
    result = await index_multiple_pdfs(ctx, papers)
    print("Resultado indexación:")
    print(result)

    print("\nIniciando búsqueda de prueba...")
    query = "complex-valued Deep Operator Network DeepONet Three Dimensional Maxwell's equations high frequency"
    search_res = search_knowledge(query, n_results=3)
    print(search_res)

if __name__ == "__main__":
    asyncio.run(main())
