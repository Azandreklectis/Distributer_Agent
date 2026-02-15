from typing import Dict, Optional

from app.tools.kb_search import search_product_knowledge


def check_price_and_margin(sku: str) -> Optional[Dict[str, str]]:
    records = search_product_knowledge(sku, where={"sku": sku})
    if not records:
        return None

    metadata = records[0]["metadata"]
    return {
        "sku": sku,
        "mrp": str(metadata.get("mrp", "unknown")),
        "distributor_price": str(metadata.get("distributor_price", "unknown")),
        "retailer_margin_percent": str(metadata.get("retailer_margin_percent", "unknown")),
        "moq": str(metadata.get("moq", "unknown")),
    }
