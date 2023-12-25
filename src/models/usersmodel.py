from sqlalchemy import event
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP 
from sqlalchemy.sql.expression import text
from src.database.db import Base
from .basemodel import BaseModel

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
