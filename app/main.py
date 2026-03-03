from fastapi import FastAPI
from . import models
from app.database import Base, engine
from app.routers import auth
app = FastAPI()

Base.metadata.create_all(bind=engine)

#Incluimos los routers:
app.include_router(auth.router)
