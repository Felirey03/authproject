from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from app.database import get_db
from app.schemas import UserCreate, UserResponse
from app.models import  User
from app.security import hash_password

router = APIRouter(prefix="/auth", tags=["auth"])

#Creamos el endpoint que, recibe el UserCreate, y guarda todos los datos necesarios
#a la DB.
@router.post("/register",response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    hashed_pw = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



