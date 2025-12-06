from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # API Settings
    APP_NAME: str = "Quant Crew"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Tavily Configuration
    TAVILY_API_KEY: str

    # Groq LLM Configuration
    GROQ_API_KEY: str
    GROQ_LLM_PROVIDER: str = "groq"
    GROQ_MODEL: str = "mixtral-8x7b-32768"  # Fast and capable model
    GROQ_MAX_TOKENS: int = 2048
    GROQ_TEMPERATURE: float = 0.3

    # Rate Limiting & Performance
    MAX_CONCURRENT_REQUESTS: int = 10
    REQUEST_TIMEOUT: int = 60
    CACHE_TTL: int = 3600  # 1 hour cache

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
