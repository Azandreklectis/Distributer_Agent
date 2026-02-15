from typing import Optional

from pydantic import BaseModel


class ChatRequest(BaseModel):
    shopkeeper_id: str
    message: str
    language: Optional[str] = "en"


class ChatResponse(BaseModel):
    reply: str
    confidence_note: str
