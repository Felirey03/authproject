from pydantic import BaseModel, EmailStr
from pydantic import UUID4
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id:UUID4
    name:str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

#Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

#Esquema para la respuesta del token
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Esquema para los datos que guardaremos en el token (opcional pero útil)
class TokenData(BaseModel):
    email: str | None = None

