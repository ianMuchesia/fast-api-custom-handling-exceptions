from pydantic import BaseModel,ConfigDict
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
    model_config = ConfigDict(from_attributes = True)

    id:str
    username: str
    email: EmailStr
    created_at: datetime
   
    
        
        
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    model_config = ConfigDict(from_attributes = True)

    id: int
    internal_id: str
    created_at: datetime
    updated_at: datetime
  
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
   
        
class UserLoginResponse(BaseModel):
    model_config = ConfigDict(from_attributes = True)

    access_token: str
    token_type: str
  
        
class Token(BaseModel):
    access_token: str
    token_type: str
   
   
class TokenData(BaseModel):
    model_config = ConfigDict(from_attributes = True)

    user_email: Optional[str] = None
    user_id: Optional[str] = None
 