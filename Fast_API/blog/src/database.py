from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# Database Connection 
DB_URl = "postgresql://postgres:root@localhost:5432/blogdb"
engine = create_engine(DB_URl)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()