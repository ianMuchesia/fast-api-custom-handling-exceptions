from pydantic import BaseModel
from typing import Optional
from datetime import datetime


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
    id:str
    created_at: datetime
    updated_at: datetime
    class Config():
        from_attributes = True
        
        
class JobUpdate(JobBase):
    pass


class JobInDBBase(JobBase):
    id: int
    internal_id: str
    created_at: datetime
    updated_at: datetime
    class Config():
        from_attributes = True
    
