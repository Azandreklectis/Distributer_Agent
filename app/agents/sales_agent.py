from pathlib import Path

from langchain_core.prompts import ChatPromptTemplate

from app.services.llm import get_chat_llm
from app.tools.kb_search import search_product_knowledge


class SalesAgent:
    """Conversational agent that answers shopkeeper queries and nudges toward order intent."""

    def __init__(self) -> None:
        prompt_path = Path("app/prompts/sales_system_prompt.txt")
        system_prompt = prompt_path.read_text(encoding="utf-8")

        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                (
                    "human",
                    "Shopkeeper ID: {shopkeeper_id}\n"
                    "Language: {language}\n"
                    "User message: {message}\n\n"
                    "Retrieved context:\n{context}\n\n"
                    "Respond to the shopkeeper.",
                ),
            ]
        )
        self.llm = get_chat_llm(temperature=0.3)

    def reply(self, shopkeeper_id: str, message: str, language: str = "en") -> dict:
        retrieved = search_product_knowledge(message)
        context = "\n\n".join(
            [f"- {item['content']}" for item in retrieved]
        ) or "No matching product records found."

        chain = self.prompt | self.llm
        output = chain.invoke(
            {
                "shopkeeper_id": shopkeeper_id,
                "language": language,
                "message": message,
                "context": context,
            }
        )

        confidence_note = (
            "Grounded in product KB."
            if retrieved
            else "Limited KB match; response may be generic."
        )
        return {
            "reply": output.content,
            "confidence_note": confidence_note,
        }
