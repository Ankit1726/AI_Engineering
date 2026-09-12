from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    content: str

class BlogResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True  # Crucial for SQLAlchemy model parsin

class BlogPagination(BaseModel):
    page: int
    limit: int
    total: int
    data: list[BlogResponse]