# Response Model : Defines Structure & Filtering Rules .

from  fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Core Database [stored senstive data]
class UserDB(BaseModel):
     name:str
     age:int 
     password:str

# Tailored Schema 
class UserResponse(BaseModel):
     name:str
     age:int 

# Assign Filtering Layer 
@app.get("/user",response_model=UserResponse)
def get_user():
     db_record = {
          "name":"Ankit",
          "age":22,
          "password":"secret_123242"
     }
     return db_record
     