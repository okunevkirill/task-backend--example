from sqlalchemy.orm import Session

from .models import User
from .schemas import UserInputSchema


def get_users(session: Session, skip: int = 0, limit: int = 100, gender=None):
    if gender:
        return session.query(User).filter_by(gender=gender).offset(skip).limit(limit)
    return session.query(User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(User).get(user_id)


def add_user(session: Session, data: UserInputSchema):
    user = User(**data.dict())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
