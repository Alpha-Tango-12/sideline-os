from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    environment: str = "development"
    database_url: str = "sqlite+aiosqlite:///./sideline_os.db"
    secret_key: str = "dev-only-insecure-key-override-in-.env"
    access_token_expire_minutes: int = 60 * 12
    cors_allow_origins: list[str] = ["http://localhost:5173"]

    @property
    def is_production(self) -> bool:
        return self.environment == "production"


@lru_cache
def get_settings() -> Settings:
    return Settings()
