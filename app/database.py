import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

#Cargamos variables del env
load_dotenv()

#CONECTAMOS BASE DE DATOS.
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

#LA SESSION PARA HACER QUERIES
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#ES LA CLASE QUE USAN LOS MODELOS
Base = declarative_base()


#INYECTAMOS LA DEPENDENCIA PARA LAS RUTAS, ESTO SIGNIFICA QUE A MEDIDA QUE SE ABRE UNA SESION, EJECUTA LAS TAREAS Y LUEGO CIERRA
#ESTA SESION AUTOMATICAMENTE
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()