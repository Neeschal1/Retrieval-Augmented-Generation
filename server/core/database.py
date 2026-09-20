from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from sqlalchemy.orm import Session
from env_config import Config

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=Config.DB_USERNAME,
    password=Config.DB_PASSWORD,
    host=Config.DB_HOST,
    port=int(Config.DB_PORT),
    database=Config.DB_NAME,
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind = engine, 
    autoflush = False, 
    autocommit = False
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependencies = Annotated[Session, Depends(get_db)]