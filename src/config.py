from functools import lru_cache
from pathlib import Path

from dotenv import find_dotenv
from pydantic import BaseSettings, conint, StrictStr, SecretStr


class Settings(BaseSettings):
    POSTGRES_HOST: StrictStr
    POSTGRES_PORT: conint(ge=1024, le=65535)
    POSTGRES_USER: StrictStr
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DATABASE_NAME: StrictStr
    POSTGRES_DATA_VOLUME: Path

    class Config:
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache
def get_settings(env_file: str = ".env") -> Settings:
    """Возвращает объект со значениями из файла для переменных окружения."""
    return Settings(_env_file=find_dotenv(env_file))
