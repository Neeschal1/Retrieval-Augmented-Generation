import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    
    SECRET_KEY = os.getenv('SECRET_KEY')
    HASH_ALGORITHM = os.getenv('HASH_ALGORITHM')
    ACCESS_TOKEN_EXPIRY = os.getenv('ACCESS_TOKEN_EXPIRY')
    REFRESH_TOKEN_EXPIRY = os.getenv('REFRESH_TOKEN_EXPIRY')