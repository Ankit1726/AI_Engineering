## Sqilte Integration 
import sqlite3 
from fastapi import FastAPI

app = FastAPI()

# Establish Connection 
conn = sqlite3.connect("data.db",check_same_thread=False)
cursor = conn.cursor()

# Make DB Table 
cursor.execute("""
         CREATE TABLE IF NOT EXISTS todos(
               id INETEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               completed TEXT DEFAULT 'false
          )
""")
conn.commit()

# endpoint for verification 
@app.post("/")
def home():
     return{
          "message":"SQLite Connected ✅"
     }