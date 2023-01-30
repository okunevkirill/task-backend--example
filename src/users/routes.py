from typing import List, Optional
from fastapi import APIRouter, status, Depends, Query

from sqlalchemy.orm import Session

from src.database import get_db_session
from . import services, schemas

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[schemas.UserOutputSchema])
async def get_users(skip: int = Query(default=0, ge=0,
                                      description="Число пропускаемых пользователей"),
                    limit: int = Query(default=100, ge=0,
                                       description="Максимальное число выводим элементов"),
                    gender: Optional[schemas.GenderType] = Query(
                        default=None,
                        description=("Фильтр по заданию пола пользователя: "
                                     "**M** - мужской, **W** - женский,"
                                     "**U** - не указан.")
                    ),
                    session: Session = Depends(get_db_session)):
    """Получить список пользователей."""
    users = services.get_users(session, skip=skip, limit=limit, gender=gender)
    return [schemas.UserOutputSchema.from_orm(obj) for obj in users]


@router.post("/",
             response_model=schemas.UserOutputSchema,
             status_code=status.HTTP_201_CREATED)
async def add_user(data: schemas.UserInputSchema,
                   session: Session = Depends(get_db_session)):
    """Создать нового пользователя."""
    user = services.add_user(session, data=data)
    return schemas.UserOutputSchema.from_orm(user)
