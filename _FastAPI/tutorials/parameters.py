from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Defining Pydantic Schema 
class Address(BaseModel):
     city:str
     pin_code:int

# Nested Modeling 
class User(BaseModel):
     name:str
     age:int
     email:str
     address:Address

@app.post("create-user")
def create_user(user:User):
     return{
          "message":"user created successfully..!",
          "data":user,
     }


# Home Route 
@app.get("/")
def home():
     return {
          "message":"Welcome TO FastAPI"
}

# Optional Parameters 
@app.get("/users")
def get_users(name:str=None):
     return {'name':name}

# Query Parameter Default Value 
@app.get("/product")
def get_products(limit:int=10):
     return {
          "limit":limit
     }

# Multiple Query Params 
@app.get("/items")
def get_items(name:str=None,price:int=0):
     return {
          "name":name,
          "price":price
     }

## [Path,Parameter,Query]
users = []

class User(BaseModel):
     name:str 
     age:int  

# Create Route 
@app.post("/users")
def create_user(user:User):
     users.append(user)
     return {
          "message":"User Created Sucess..",
          "data":user
     }

# Update Route [mapping with (Path,Query,Body)]
@app.put("/users/{user_id}")
def update_user(
     user_id:int,  # Path
     user:User,    # Request
     notify:bool = False  # Body
):
     if user_id < len(users):
          users[user_id] = user 
          return{
            "message": "User updated", 
            "notify_status": notify, 
            "data": user
          }
     return {"error":"user not found"}