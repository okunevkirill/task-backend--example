from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config import get_settings

SETTINGS = get_settings()

DATABASE_URL = (
    "postgresql+psycopg2:"
    f"//{SETTINGS.POSTGRES_USER}:"
    f"{SETTINGS.POSTGRES_PASSWORD.get_secret_value()}"
    f"@{SETTINGS.POSTGRES_HOST}:{SETTINGS.POSTGRES_PORT}"
    f"/{SETTINGS.POSTGRES_DATABASE_NAME}"
)

engine = create_engine(DATABASE_URL)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def init_models():
    """Инициализация создания таблиц базы данных"""
    Base.metadata.create_all(bind=engine)


def get_db_session():
    """Возвращает сессию подключения к базе данных"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
