from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from slowapi import Limiter,_rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

app = FastAPI()

# Initialise Rate Limiter 
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# Register Global Handler 
@app.exception_handler(RateLimitExceeded)
def limit_handler(request:Request,exc:RateLimitExceeded):
     return JSONResponse(
          status_code=429,
          content={
               "detail":"too many requests..! slow down pls"
          }
     )

# Apply Limiter To Specific Route 
@app.get("data")
@limiter.limit("1/minute")
def get_data(request:Request):
     return {
          "message":"Success✅ Here is your data..!"
     }