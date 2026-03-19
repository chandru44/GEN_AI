from app.repositories.knowledge_base import SECURITY_KB


def search_knowledge(query: str) -> dict:
    matches = [doc for doc in SECURITY_KB if any(word in doc['content'].lower() or word in doc['title'].lower() for word in query.lower().split())]
    return {"query": query, "results": matches[:5]}
