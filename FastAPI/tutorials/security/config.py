import os 
from dotenv import load_dotenv
load_dotenv()

# Config For Security Layer
class Settings:
    SECRET_KEY:str = os.getenv("SECRET_KEY","fallback_!@#")
    DATABASE_URL:str = os.getenv("DATABASE_URL","sqlite:///./default.db")
    ALLOWED_ORIGIN:str = os.getenv("ALLOWED_ORIGIN","http://localhost:3000")

settings = Settings()