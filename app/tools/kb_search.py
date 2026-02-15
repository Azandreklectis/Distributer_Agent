import re
from typing import Any, Dict, List, Optional

from app.core.settings import get_settings
from app.services.vector_store import get_vector_store


def normalize_sku(value: str) -> str:
    return re.sub(r"\s*-\s*", "-", value.strip().upper())


def extract_sku_from_query(query: str) -> Optional[str]:
    """Extract patterns like BIS-001 or BIS - 001 from free text."""
    match = re.search(r"\b([A-Za-z]{2,6})\s*-\s*(\d{2,6})\b", query)
    if not match:
        return None
    return normalize_sku(f"{match.group(1)}-{match.group(2)}")


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


def search_product_by_sku(sku: str) -> List[Dict[str, Any]]:
    normalized = normalize_sku(sku)
    return search_product_knowledge(normalized, where={"sku": normalized})
