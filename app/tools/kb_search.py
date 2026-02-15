from typing import Any, Dict, List

from app.core.settings import get_settings
from app.services.vector_store import get_vector_store


def search_product_knowledge(query: str, where: Dict[str, Any] | None = None) -> List[Dict[str, Any]]:
    settings = get_settings()
    store = get_vector_store()
    docs = store.similarity_search(query, k=settings.top_k, filter=where)
    results: List[Dict[str, Any]] = []
    for doc in docs:
        results.append(
            {
                "content": doc.page_content,
                "metadata": doc.metadata,
            }
        )
    return results
