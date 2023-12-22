from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic import EmailStr  

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    
    
class UserCreate(UserBase):
    pass


class UserResponse(BaseModel):
    id:str
    username: str
    email: EmailStr
    created_at: datetime
   
    class Config():
        from_attributes = True
        
        
        
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: int
    internal_id: str
    created_at: datetime
    updated_at: datetime
    class Config():
        from_attributes = True
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
   
        
class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str
    class Config():
        from_attributes = True
        
        
class Token(BaseModel):
    access_token: str
    token_type: str
   
   
class TokenData(BaseModel):
    user_email: Optional[str] = None
    user_id: Optional[str] = None
    class Config():
        from_attributes = True
        