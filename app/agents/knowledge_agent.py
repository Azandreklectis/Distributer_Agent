from typing import List

from langchain_core.documents import Document

from app.schemas.product import Product
from app.services.vector_store import get_vector_store


class KnowledgeAgent:
    """Builds and updates a product knowledge base in vector storage."""

    def __init__(self) -> None:
        self.store = get_vector_store()

    @staticmethod
    def _to_document(product: Product) -> Document:
        offers_text = ", ".join(product.offers or [])
        benefits_text = ", ".join(product.benefits)
        content = (
            f"SKU: {product.sku}\n"
            f"Name: {product.name}\n"
            f"Category: {product.category}\n"
            f"MRP: {product.mrp}\n"
            f"Distributor price: {product.distributor_price}\n"
            f"Retailer margin: {product.retailer_margin_percent}%\n"
            f"MOQ: {product.moq}\n"
            f"Shelf life days: {product.shelf_life_days}\n"
            f"Benefits: {benefits_text}\n"
            f"Offers: {offers_text or 'none'}"
        )
        metadata = product.model_dump()
        return Document(page_content=content, metadata=metadata)

    def upsert_products(self, products: List[Product]) -> int:
        docs = [self._to_document(product) for product in products]
        ids = [product.sku for product in products]
        self.store.add_documents(docs, ids=ids)
        return len(products)
