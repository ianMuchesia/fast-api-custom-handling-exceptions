from jose import jwt, JWTError
from datetime import datetime, timedelta
from ..errors import forbidden  as Forb, notfound
from ..schemas.user_schemas import TokenData
from decouple import config
from fastapi import Request
from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import db
from ..models.basemodel import User
from ..config.config import settings

#SECRET KEY
SECRET_KEY = settings.SECRET_KEY
ALGORITHM =   settings.ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    #this is where we will create the token
    to_encode = data.copy()

    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


def verify_access_token(token:str):
    #this is where we will verify the token
    try:
        payload =jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    
        payload_email = payload.get("user_email")
        payload_id:str = payload.get("user_id")
    
        if payload_email is None or payload_id is None:
            raise Forb.ForbiddenError("Invalid Credentials")
    
        token_data = TokenData(user_email=payload_email, user_id=payload_id)
    
        return token_data
    except JWTError:
        raise Forb.ForbiddenError("Invalid Credentials")
    
    
    
def get_current_user(req:Request, db:Session = Depends(db.get_db)):
    #this is where we will get the token from the request header
    if "Authorization" not in req.headers:
        raise Forb.ForbiddenError("Not authenticated")
    token = req.headers["Authorization"]
 
    token = token.replace("Bearer ", "")
  
    token_data = verify_access_token(token)
    user_id = token_data.user_id
   
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise notfound.NotFoundError("User not found")
    return db_user
 