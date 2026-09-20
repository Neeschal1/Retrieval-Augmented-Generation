from fastapi import FastAPI, APIRouter
from routes.auth import userrouter
from core.database import Base, engine
from env_config import Config
from models.users import User

app = FastAPI()

app.include_router(userrouter)

# @app.get("/")
# def homepage():
#     return {"message": "Hello World!"}

print("USERNAME:", Config.DB_USERNAME)
print("HOST:", Config.DB_HOST)
print("PORT:", Config.DB_PORT)
print("DATABASE:", Config.DB_NAME)


Base.metadata.create_all(bind=engine)