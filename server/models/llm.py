from sqlalchemy import String, Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from core.database import Base

class APIKey(Base):
    __tablename__ = "Llmapi"
    
    id = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, ForeignKey("Users.id"), nullable=False)
    key = Column(String(255), nullable=False)
    createdat = Column(DateTime, server_default=func.now(), nullable=False)