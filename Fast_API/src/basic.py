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
def gey_users(name:str=None):
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
