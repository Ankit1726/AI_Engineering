import requests 
from fastapi import FastAPI,HTTPException,status 

app = FastAPI()
EXTERNAL_API = "https://jsonplaceholder.typicode.com/posts"

# Fetching All Records 
@app.get("/posts")
def get_posts():
     response = requests.get(EXTERNAL_API)
     return response.json()

# Fetch Using Id 
@app.get("/posts/{post_id}")
def get_post_id(post_id:int):
     targetd_url = f"{EXTERNAL_API}/{post_id}"
     response = requests.get(targetd_url)

     if response.status_code!=200:
          raise Exception(
               status_code = status.HTTP_404_NOT_FOUND,
               detail = "data not found...!"
          )
     return response.json()
