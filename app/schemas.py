from app.database import Base
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    class Config:
            orm_mode = True


class PostCreate(PostBase):
    pass
    class Config:
            orm_mode = True


class Post(PostBase):
    id: int
    # title: str
    # content: str
    # published: bool = True
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True