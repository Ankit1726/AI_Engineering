from fastapi import FastAPI, Depends
from src.database import get_db
from src.schemas import BlogCreate
from sqlalchemy.orm import Session
from src.database import engine
from src import models, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Home Route
@app.get("/")
def home():
    return {"message": "Blog API running..✅"}


## CRUD Operations
# Create Blog
@app.post("/create-blogs")
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, content=blog.content)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# Read Blogs
@app.get("/blogs", response_model=list[schemas.BlogResponse])
def get_blogs(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()