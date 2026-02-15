import json
from pathlib import Path

from app.schemas.product import Product

CATALOG_PATH = Path("data/sample_products.json")


def load_catalog() -> list[Product]:
    if not CATALOG_PATH.exists():
        return []
    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    return [Product(**item) for item in data]
