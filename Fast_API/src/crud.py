# CURD Operation (Create,Update,Read,delete)
from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()
todos = [] # short storage memory 

# Pydantic Schema 
class Todo(BaseModel):
     id:int
     title:str
     completed:bool


# Create [POST]
@app.post("/todos")
def create_todos(todo:Todo):
     todos.append(todo)
     return{
          "message":"Todo Added",
          "data":todo
     }

# Read [GET]
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
     for todo in todos:
          if todo.id == todo_id:
               return todo 
     return{
          "error":"Todo Not Found"
     }

# Update [PUT]
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
     for i,todo in enumerate(todos):
          if todo.id == todo_id:
               todos[i] = updated_todo
               return {
                    "message":"Data pdated Success..!",
                    "data":update_todo
               }
     return {"error":"Todo Not Found..!"}

# Delete [DELETE]
@app.delete("/todo/{todo_id}")
def delete_todo(todo_id:int):
     for i,todo in enumerate(todos):
          if todo.id == todo_id:
               todos.pop(i)
               return{
                    "message":"Data Deleted Success..!"
               }
     return {"error","Data Not Found"}

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