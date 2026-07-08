## Asynchronous Programming:
"""Asynchronous programming is a non-blocking execution approach that allows a single server process to manage multiple incoming requests concurrently 
without waiting for previous tasks to finish entirely."""

# Traditional Synchronous (Blocking)
import time 
def blocking_task():
     time.sleep(2)
     return "Done"

# Modern Asynchronous (Non-Blocking)
import asyncio
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def async_home():
     await asyncio.sleep(3)
     return {"message": "Async API response successful✅"}