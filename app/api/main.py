from functools import lru_cache

from fastapi import FastAPI, HTTPException

from app.agents.knowledge_agent import KnowledgeAgent
from app.agents.sales_agent import SalesAgent
from app.schemas.chat import ChatRequest, ChatResponse
from app.schemas.product import ProductBatch

app = FastAPI(title="Distributor Agent API", version="0.1.0")


@lru_cache
def get_knowledge_agent() -> KnowledgeAgent:
    return KnowledgeAgent()


@lru_cache
def get_sales_agent() -> SalesAgent:
    return SalesAgent()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/kb/products")
def upsert_products(batch: ProductBatch) -> dict:
    count = get_knowledge_agent().upsert_products(batch.products)
    return {"indexed": count}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    try:
        result = get_sales_agent().reply(
            shopkeeper_id=request.shopkeeper_id,
            message=request.message,
            language=request.language or "en",
        )
        return ChatResponse(**result)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
