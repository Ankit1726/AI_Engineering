from fastapi import FastAPI, Depends,HTTPException,status
from src.database import get_db
from src.schemas import BlogCreate,BlogResponse
from sqlalchemy.orm import Session
from src.database import engine
from src import models, schemas
from src.auth import create_access_token,verify_token

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Login Endpoint 
@app.post("/login")
def login():
    access_token = create_access_token(data={"sub":"admin_user"})
    return {
        "access_token": access_token,
        "token_type":"bearer"
    }

# Home Route
@app.get("/")
def home():
    return {"message": "Blog API running..✅"}

## CRUD Operations
# Read Blogs
@app.get("/blogs", response_model=list[schemas.BlogResponse])
def get_blogs(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()

# Create Blog
@app.post("/create-blogs")
def create_blog(blog: BlogCreate, db: Session = Depends(get_db),user = Depends(verify_token)):
    new_blog = models.Blog(title=blog.title, content=blog.content)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# Read Blog By id 
@app.get("/blogs/{id}",response_model=BlogResponse)
def get_blog(id:int,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Blog Not Found"
        )
    return blog

# Update Blog 
@app.put("/blogs/{id}",response_model=BlogResponse)
def update_blog(id:int,blog_input:BlogCreate,db:Session = Depends(get_db),user = Depends(verify_token)):
    existing_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not existing_blog:
        raise HTTPException(status_code=404, detail="Blog Not Found ❎")
    
    existing_blog.title = blog_input.title
    existing_blog.content = blog_input.content
    db.commit()
    return existing_blog

# Delete Blog 
@app.delete("/blogs/{id}")
def delete_blog(id:int,db:Session = Depends(get_db),user = Depends(verify_token)):
    del_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not del_blog:
        raise HTTPException(status_code=404, detail="Blog Not Found")
    db.delete(del_blog)
    db.commit()
    return {"message": "Blog deleted successfully"}