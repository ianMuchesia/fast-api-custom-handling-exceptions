from jose import jwt, JWTError
from datetime import datetime, timedelta
from ..errors import forbidden  as Forb
from ..schemas.user_schemas import TokenData
from decouple import config



#SECRET KEY
SECRET_KEY = config("SECRET_KEY")
ALGOTITHM =  config("ALGOTITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES ")

def create_access_token(data: dict):
    to_encode = data.copy()

    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGOTITHM)
    
    return encoded_jwt


def verify_access_token(token:str):
    payload =jwt.decode(token, SECRET_KEY, algorithms=[ALGOTITHM])
    
    payload_email = payload.get("user_email")
    payload_id = payload.get("user_id")
    
    if payload_email is None or payload_id is None:
        raise Forb.ForbiddenError("Invalid Credentials")
    
    token_data = TokenData(user_email=payload_email, user_id=payload_id)
    
    return token_data
    
