from ingest import kb  # matches the exported name in ingest.py
from agno.agent import Agent



agent = Agent(
    name="LegalDocRAGAgent",
    description=(
        "A RAG-powered agent that answers legal questions using a PDF knowledge base. "
        "It retrieves relevant document snippets, reasons over them, and cites exact sources."
    ),
    instructions="""
You are a legal expert assistant. When given a question:
1. Search the Knowledge Base.
2. Use the retrieved context to craft a clear, accurate answer.
3. Give Answer in as much detail as you can proper structure way.
4. Cite the sources (e.g., snippet text or page numbers).
5. If unsure, explicitly say “I don’t know”.

Always ground your answer in the retrieved documents and avoid hallucination.
    """.strip(),
    knowledge=kb,

    search_knowledge=True,
)



# agent.knowledge.load(recreate=False)
def answer(question:str):

    response = agent.run(question)
    return response.content

