import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

URL = "https://indianexpress.com"


@app.get("/news")
def get_news():
     response = requests.get(URL)
     soup = BeautifulSoup(response.text,"html.parser")
     headline_list = []
     target_element = soup.find_all("a",class_="")

     for i in target_element:
          headline_list.append(i.text.strip())
          return {"headline":headline_list[:7]}