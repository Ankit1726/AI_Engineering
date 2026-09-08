from fastapi import FastAPI, Depends, HTTPException, status, Header
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


# ------------------ Token Creation ------------------ #
def create_access_token(data: dict):
    encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    )

    encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        encode,
        os.getenv("SECRET_KEY"),
        algorithm=os.getenv("ALGORITHM")
    )

    return encoded_jwt


# ------------------ Verify Token ------------------ #
def verify_token(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization header"
        )

    try:
        scheme, token = authorization.split()

        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme"
            )

        payload = jwt.decode(
            token,
            os.getenv("SECRET_KEY"),
            algorithms=[os.getenv("ALGORITHM")]
        )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )


# ------------------ Login ------------------ #
@app.post("/login")
def login(username: str, password: str):
    if username != "admin" or password != "12345":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    token = create_access_token({"sub": username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ------------------ Protected Route ------------------ #
@app.get("/secure")
def get_secure_data(current_user: dict = Depends(verify_token)):
    return {
        "message": "Secure dataset access granted successfully!",
        "user_info": current_user
    }