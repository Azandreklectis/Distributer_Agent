from functools import lru_cache

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException

from app.agents.knowledge_agent import KnowledgeAgent
from app.agents.sales_agent import SalesAgent
from app.schemas.chat import ChatRequest, ChatResponse
from app.schemas.product import ProductBatch
from app.services.catalog import load_catalog

app = FastAPI(title="Distributor Agent API", version="0.2.0")
app.mount("/static", StaticFiles(directory="app/web/static"), name="static")
templates = Jinja2Templates(directory="app/web/templates")

app = FastAPI(title="Distributor Agent API", version="0.1.0")


@lru_cache
def get_knowledge_agent() -> KnowledgeAgent:
    return KnowledgeAgent()


@lru_cache
def get_sales_agent() -> SalesAgent:
    return SalesAgent()


@app.on_event("startup")
def warm_knowledge_base() -> None:
    catalog = load_catalog()
    if not catalog:
        return
    try:
        get_knowledge_agent().upsert_products(catalog)
    except Exception:
        # Keep the web app running even if AI dependencies/env are not ready yet.
        return


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    catalog = load_catalog()
    return templates.TemplateResponse(
        request,
        "index.html",
        {"products": catalog, "reply": None, "question": ""},
    )


@app.post("/ask", response_class=HTMLResponse)
def ask_question(request: Request, question: str = Form(...)) -> HTMLResponse:
    catalog = load_catalog()
    try:
        result = get_sales_agent().reply(
            shopkeeper_id="web-user",
            message=question,
            language="en",
        )
    except Exception as exc:
        result = {
            "reply": f"Unable to answer right now: {exc}",
            "confidence_note": "Service error",
        }

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "products": catalog,
            "reply": result,
            "question": question,
        },
    )


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
