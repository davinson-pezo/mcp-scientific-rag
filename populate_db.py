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
    papers = [
        os.path.expanduser('~/Documents/references/Lu_2021_DeepONet.pdf'),
        os.path.expanduser('~/Documents/references/Jagtap_2020_XPINN.pdf'),
        os.path.expanduser('~/Documents/references/Shukla_2021_ParallelPINN.pdf'),
        os.path.expanduser('~/Documents/references/Jiang_2024_Maxwell_DeepONet.pdf')
    ]
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
