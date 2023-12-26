from sqlalchemy import event
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP 
from .basemodel import BaseModel,Base


from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Job(BaseModel, Base):
    __tablename__ = "jobs"

    # No need to redefine internal_id, it is inherited from BaseModel
    title = Column(String)
    company = Column(String)
    company_url = Column(String, nullable=True)
    location = Column(String)
    description = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    is_active = Column(Boolean, default=True)
    
    user_id = Column(String, ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
   
    user = relationship("User")
    @classmethod
    def before_update_listener(cls, mapper, connection, target):
        BaseModel.before_update_listener(mapper, connection, target)

# Use event.listen with the correct event name
event.listen(Job, 'before_update', Job.before_update_listener)


