from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings  

app = FastAPI()

origins = [
    settings.ALLOWED_ORIGIN
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home_route():
    return {
        "status": "Online",
        "database_target": settings.DATABASE_URL,
        "message": "Environment settings loaded perfectly!"
    }
