from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello AI Dev Ankit"
    }

@app.get("/add")
def add_nums(a: int, b: int):
    return {
        "result": a + b
    }