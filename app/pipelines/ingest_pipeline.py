import json
from pathlib import Path

from app.agents.knowledge_agent import KnowledgeAgent
from app.schemas.product import Product


def ingest_products_json(path: str) -> int:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    products = [Product(**item) for item in data]
    return KnowledgeAgent().upsert_products(products)
