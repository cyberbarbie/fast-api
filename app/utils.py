from passlib.context import CryptContext
# specify default hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    """check whether password verifies against the hash"""
    return pwd_context.verify(plain_password, hashed_password)