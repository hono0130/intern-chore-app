from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from datetime import datetime, timedelta

from models.model import User
import schemas.user as user_scheme
from cruds.user import get_user_by_email, get_user_by_id

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate(email: str, password: str) -> user_scheme.UserUpdate: 
    user = get_user_by_email(email) #後で作る(crud/user.py)
    if user.password != password:
        raise HTTPException(status_code=401, detail="パスワード不一致")
    return user

def create_tokens(user_id: int):
    access_payload = {
        "token_type": "access_token",
        "exp": datetime.utcnow() + timedelta(minutes=60),
        "user_id": user_id
    }
    
    access_token = jwt.encode(access_payload, "SECRET_KEY123", algorithm="HS256")

    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user_from_token(token: str, token_type: str):
    
    payload = jwt.decode(token, 'SECRET_KEY123', algorithms=["HS256"])

    if payload["token_type"] != token_type:
        raise HTTPException(status_code=401, detail="トークンタイプ不一致")

    user = get_user_by_id(payload["user_id"]) #後で作る(crud/user.py)
    
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    return get_current_user_from_token(token, "access_token")
