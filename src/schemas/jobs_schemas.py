from pydantic import BaseModel,ConfigDict
from typing import Optional
from datetime import datetime
from .user_schemas import UserResponse

class JobBase(BaseModel):
    title: str
    company: str
    company_url: Optional[str] = None
    location: str
    description: str
    is_active: Optional[bool] = True
    
    
class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    model_config = ConfigDict(from_attributes = True)
    id:str
    created_at: datetime
    updated_at: datetime
    user_id:str
    user:UserResponse
  
        
        
class JobUpdate(JobBase):
    pass


class JobInDBBase(JobBase):
    model_config = ConfigDict(from_attributes = True)

    id: int
    internal_id: str
    created_at: datetime
    updated_at: datetime

    
