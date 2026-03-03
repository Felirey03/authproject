from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)


#Funcion para hashear password
def hash_password(password: str)->str:
    return pwd_context.hash(password)


#Funcion para verificar password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
