from langchain_chroma import Chroma

from app.core.settings import get_settings
from app.services.llm import get_embeddings


def get_vector_store(collection_name: str = "products") -> Chroma:
    settings = get_settings()
    return Chroma(
        collection_name=collection_name,
        embedding_function=get_embeddings(),
        persist_directory=settings.chroma_dir,
    )
