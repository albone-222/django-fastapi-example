import os
from typing import Any, Dict, Optional

from dotenv import load_dotenv
from pydantic import Field, HttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings

load_dotenv()


class DBSettings(BaseSettings):
    POSTGRES_HOST: str = Field(default=os.getenv("POSTGRES_HOST", default="localhost"))
    POSTGRES_PORT: int = Field(default=os.getenv("POSTGRES_PORT", default=5432))
    POSTGRES_USER: str = Field(default=os.getenv("POSTGRES_USER", default="postgres"))
    POSTGRES_PASSWORD: str = Field(
        default=os.getenv("POSTGRES_PASSWORD", default="12345")
    )
    POSTGRES_DB: str = Field(default=os.getenv("POSTGRES_DB", default="postgres"))
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_url(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values["POSTGRES_USER"],
            password=values["POSTGRES_PASSWORD"],
            host=values["POSTGRES_HOST"],
            port=values["POSTGRES_PORT"],
            path=f"{values.get('POSTGRES_DB') or ''}",
        )


class Settings(BaseSettings):
    db: BaseSettings = DBSettings()


settings = Settings()
