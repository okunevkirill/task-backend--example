from pydantic import BaseModel, StrictStr, conint
from .types import GenderType


class UserInputSchema(BaseModel):
    name: StrictStr = "Anonymous"
    gender: GenderType = GenderType.UNKNOWN

    class Config:
        schema_extra = {
            "example": {
                "name": "Jules Verne",
                "gender": GenderType.MAN
            }
        }


class UserOutputSchema(BaseModel):
    id: conint(ge=1)
    name: StrictStr
    gender: GenderType = GenderType.UNKNOWN

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Jules Verne",
                "gender": GenderType.MAN
            }
        }
