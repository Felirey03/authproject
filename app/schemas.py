from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic import UUID4
from datetime import datetime

class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id:UUID4
    name:str
    email: EmailStr
    is_active: bool
    created_at: datetime