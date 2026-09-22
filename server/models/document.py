from sqlalchemy import  String, Column, Integer,  ForeignKey, Text, DateTime
from sqlalchemy.sql import func
from core.database import Base

class Docs(Base):
    __tablename__ = "Documents"
    
    id = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, ForeignKey("Users.id"), nullable=False)
    filename = Column(String(50), nullable=False)
    filetype = Column(String(10), nullable=False)
    fullcontent = Column(Text, nullable=False)
    createdat = Column(DateTime, server_default=func.now(), nullable=False)