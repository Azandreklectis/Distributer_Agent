from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    google_api_key: str = Field(alias="GOOGLE_API_KEY")
    gemini_model: str = Field(default="gemini-1.5-flash", alias="GEMINI_MODEL")
    chroma_dir: str = Field(default="./data/chroma", alias="CHROMA_DIR")
    embedding_model: str = Field(default="models/text-embedding-004", alias="EMBEDDING_MODEL")
    top_k: int = Field(default=4, alias="TOP_K")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
