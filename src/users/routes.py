from typing import List, Optional
from fastapi import APIRouter, status, Depends, Query, Path, HTTPException

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


@router.get("/{user_id}", response_model=schemas.UserOutputSchema)
def get_user(user_id: int = Path(ge=1,
                                 description="Идентификатор, под которым хранится "
                                             "информация о конкретном пользователе"),
             session: Session = Depends(get_db_session)):
    user = services.get_user(session, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return schemas.UserOutputSchema.from_orm(user)
