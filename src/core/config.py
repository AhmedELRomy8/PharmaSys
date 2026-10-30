"""Application configuration settings."""

from pydantic import BaseModel


class Settings(BaseModel):
    APP_NAME: str = "PharmaSys"
    APP_VERSION: str = "0.1.0"
    API_V1_PREFIX: str = "/api/v1"
    DATABASE_URL: str = "sqlite+aiosqlite:///./pharmasys.db"
    JWT_SECRET: str = "supersecret-hospital-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480  # 8-hour hospital shift


settings = Settings()
