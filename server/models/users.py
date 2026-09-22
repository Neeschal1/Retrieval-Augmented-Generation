from sqlalchemy import String, Column, Integer, Boolean
from core.database import Base

class User(Base):
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(255))
    email = Column(String(50), unique=True)
    username = Column(String(20), unique=True)
    password = Column(String(255))
    gender = Column(String(6))
    isactive = Column(Boolean, default=False)