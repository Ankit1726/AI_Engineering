from fastapi import FastAPI
from fastapi.middleware.cors  import CORSMiddleware

app = FastAPI()

# Define Origin Route 
origin = [
    "http://localhost:5173",
]

# Inject Cors Middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def home():
    return{
        "message":"CORS Enabled API is working smothly"
    }