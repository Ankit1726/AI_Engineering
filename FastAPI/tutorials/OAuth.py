from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

# ---------------- Configuration ---------------- #

SECRET_KEY = "production_ready_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ---------------- Fake Database ---------------- #

hashed_password = pwd_context.hash("1234")

fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": hashed_password,
    }
}

# ---------------- Helper Functions ---------------- #

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise credentials_exception

        user = fake_user_db.get(username)

        if user is None:
            raise credentials_exception

        return user

    except JWTError:
        raise credentials_exception


# ---------------- Login Route ---------------- #

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    user = fake_user_db.get(form_data.username)

    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )

    if not verify_password(
        form_data.password,
        user["hashed_password"]
    ):
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )

    access_token = create_access_token(
        {"sub": user["username"]}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ---------------- Protected Route ---------------- #

@app.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {
        "message": "Hello! You have successfully accessed the protected route.",
        "username": current_user["username"]
    }