from fastapi import FastAPI
from routes.auth import userrouter
from routes.documents import uploadeddocument
from core.database import Base, engine
from models.users import User

app = FastAPI()

app.include_router(userrouter)
app.include_router(uploadeddocument)

Base.metadata.create_all(bind=engine)