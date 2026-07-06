## HTTP Status Code 
from fastapi import FastAPI,status,HTTPException

app = FastAPI()

# user cration [status code:201]
@app.post("/create-user")
def create_user():
     return {
          "message":"user creaated sucess...✅",
          "status_code":status.HTTP_201_CREATED
     }

# Returning Custom Industrial-Grade Payload Format
@app.get("/user")
def get_user():
     return{
          "status":status.HTTP_200_OK,
          "message":"user fetched sucessfully",
          "data":{
               "name":"Ankit",
               "age":22
          }
     }

# Builtit Exception [HTTP Exception]
@app.get("/users/{user_id}")
def get_specific_user(user_id:int):
     # Validation Layer
     if user_id!=1:
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail="user not found..!"
          )
     return {
          "id":1,
          "name":"Ankit"
     }