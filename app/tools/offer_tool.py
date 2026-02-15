from typing import List

from app.tools.kb_search import search_product_knowledge


def fetch_offers(sku: str) -> List[str]:
    records = search_product_knowledge(sku, where={"sku": sku})
    if not records:
        return []
    offers = records[0]["metadata"].get("offers")
    if not offers:
        return []
    if isinstance(offers, list):
        return [str(offer) for offer in offers]
    return [str(offers)]
