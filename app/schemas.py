from pydantic import BaseModel, EmailStr
from pydantic import UUID4
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id:UUID4
    name:str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True