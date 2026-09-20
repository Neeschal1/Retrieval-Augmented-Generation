import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVER_API_URL = os.getenv('SERVER_API_URL')