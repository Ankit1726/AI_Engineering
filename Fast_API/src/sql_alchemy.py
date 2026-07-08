## Integration of SQL Alchemy 
import sqlite3
from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session

# Database Config 
DB_URL = "sqlite:///./data.db"

# Data Core Setup 
engine = create_engine(DB_URL,connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

# Define DB Table Model
class Todo(Base):
     __tablename__ = "todos"

     id = Column(Integer,primary_key=True,index=True)
     title = Column(String,nullable=False)
     completed = Column(String,default="false")

# Initialise Db Table 
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database Dependency Injector 
def get_db():
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()

# @app.get("/")
# def home(db:Session = Depends(get_db)):
#      return{
#           "message":"DB Connected Success✅"
#      }


### CRUD Operations 
# Create (POST)
@app.post("/todos")
def create_todo(title:str,db:Session=Depends(get_db)):
     new_todo = Todo(title=title,completed="false")
     db.add(new_todo)
     db.commit()
     db.refresh(new_todo)
     return{
          "message":"Todo Created ✅",
          "data":new_todo
     }

# Read(GET)
@app.get("/todos")
def get_all_todos(db:Session = Depends(get_db)):
     todos = db.query(Todo).all()
     return{
          "total":len(todos),
          "data":todos
     }

@app.get("/todos/{todo_id}")
def get_by_id(todo_id:int,db:Session = Depends(get_db)):
     todo = db.query(Todo).filter(Todo.id == todo_id).first()

     if not todo:
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detial = "Todo Not Found..!"
          )

     return todo

# Update (PUT)
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db:Session = Depends(get_db)):
     todo = db.query(Todo).filter(Todo.id == todo_id).first()

     if not todo:
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detial="Todo Not Found...!"
          )
     todo.title = title
     db.commit()
     db.refresh(todo)

     return{
          "message":"Todo Updated Successfully✅",
          "data":todo
     }

# Delete(Delete)
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session = Depends(get_db)):
     todo = db.query(Todo).filter(Todo.id == todo_id).first()

     if not todo:
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND,
               detail = "Todo Not Found..!"
          )
     db.delete(todo)
     db.commit()

     return{
          "message":"Todo Deleted Successfully✅"
     }