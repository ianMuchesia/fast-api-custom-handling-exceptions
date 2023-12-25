import uuid
from uuid import UUID
from sqlalchemy import Column,  TIMESTAMP,String,Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.expression import text
from datetime import datetime
from ..database.db import Base






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