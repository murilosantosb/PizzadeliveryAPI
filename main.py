# uvicorn main:app --reload 
from fastapi import FastAPI
from routes import router
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

app.include_router(router)