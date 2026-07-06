## Middleware 
import time 
from fastapi import FastAPI,Request

app = FastAPI()

@app.middleware("http")
async def add_performance_logging(request:Request,call_next):
     start_time = time.time()
     response = await call_next(request)
     process_duration = time.time() - start_time

     # Log out performance automatically 
     print(f"Path Routed: {request.url.path} | Time Elapse: {process_duration:.4f}s")

     return response

@app.get("/users")
def get_user_list():
     return{
          "status":"success✅",
          "data":[]
     }