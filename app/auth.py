from fastapi import Depends, HTTPException 
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from datetime import datetime , timedelta 
from jose import jwt
from passlib.context import CryptContext
from app.config import SECRET_KEY , ALGORITHM , ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated = "auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

def create_access_token(data:dict):
    to_encode = data.copy()
    expire_time =datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire_time})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


bearer_scheme = HTTPBearer()

def get_current_user(
         credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
         db:Session=Depends(get_db)
):
    try:
        token = credentials.credentials
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email:str=payload.get("sub")
    except:
        raise HTTPException(status_code=401,detail="Invalid token")
    
    user=db.query(models.User).filter(models.User.email==email).first()
    if not user:
        raise HTTPException(status_code=401,detail="User not found")
    
    return user
