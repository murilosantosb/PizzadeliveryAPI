from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os

load_dotenv()

ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE = int(os.getenv("ACCESS_TOKEN_EXPIRE"))

bcrypt_context = CryptContext(schemes=["argon2"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login")
