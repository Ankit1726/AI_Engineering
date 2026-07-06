## HTTP Exception 
from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# Define a Targeted Application-Specific Exception Class
class UserNotFound(Exception):
     def __init__(self, name:str):
          self.name = name 

# Centralized Global Exception
@app.exception_handler(UserNotFound)
def user_not_found(request:Request,exc:UserNotFound):
     return JSONResponse(
          status_code=404,
          content={
          "status": "error",
            "message": f"User '{exc.name}' could not be located in the system"
     })

# Raising Exception  
@app.get("/user/{name}")
def get_user_profile(name:str):
     if name!="Ankit":
          raise UserNotFound(name=name)

     return {
          "status":"success✅",
          "username":name
     }