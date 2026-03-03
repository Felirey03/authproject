from pydantic import BaseModel, EmailStr
from pydantic import UUID4
from datetime import datetime


#Esquema que recibe para crear el usuario
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


#Esquema de respuesta de creacion de usuario
class UserResponse(BaseModel):
    id:UUID4
    name:str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

#Esquema del login(lo que debe recibir)
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
