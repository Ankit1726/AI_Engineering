# Dependency Injection
from typing import Optional
from fastapi import FastAPI,Depends,Header,HTTPException,status

app = FastAPI()

# Reusable Dependency Component 
def verify_token(token:Optional[str]=Header(None)):
     if token != "secret_token":
          raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail="Invalid or missing authentication token"
          )
     return "authorized_user"

# Apply Security Guard 
@app.get("/secured-data")
def get_secure_vault(user:str=Depends(verify_token)):
     # execute only verify token
     return{
          "status":"success✅",
          "message": "Secure vault access granted.",
          "authenticated_as": user
     }