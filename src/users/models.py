from sqlalchemy import Column, Integer, String

from src.database import Base

from .types import GenderType


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    gender = Column(String(1), default=GenderType.UNKNOWN, nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name})"
