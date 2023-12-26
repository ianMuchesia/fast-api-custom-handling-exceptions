import uuid
from uuid import UUID
from sqlalchemy import Column,  TIMESTAMP,String,Integer,Boolean,ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.expression import text
from datetime import datetime

from sqlalchemy import event





Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    internal_id = Column(Integer, primary_key=True, autoincrement=True)  # Internal primary key
    id = Column(String, unique=True, nullable=False, index=True, default=str(uuid.uuid4()))  # External/public ID for API/frontend
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

    @classmethod
    def before_update_listener(cls, mapper, connection, target):
        target.updated_at = datetime.utcnow()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        
        
        
        
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


class User(BaseModel, Base):
    __tablename__ = "users"

    # No need to redefine id and internal_id, they are inherited from BaseModel
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

    phone_number = Column(String, unique=True)
    @classmethod
    def before_update_listener(cls, mapper, connection, target):
       BaseModel.before_update_listener(mapper, connection, target)

# Register the event listener for the before_update event
event.listen(User, 'before_update', User.before_update_listener)
