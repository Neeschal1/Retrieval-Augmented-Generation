from fastapi import status, APIRouter, HTTPException
from models.users import User as UserDB
from schemas.auth import UserSignup as UserSchemas
from core.database import db_dependencies

userrouter = APIRouter(prefix='/users', tags=['Authentications'])

@userrouter.post('/create-users/', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependencies, user: UserSchemas):
    try:
        userdata = user.model_dump()
        existing_email = db.query(UserDB).filter(user.email == UserDB.email).first()
        if existing_email:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")
        
        existing_username = db.query(UserDB).filter(user.username == UserDB.username).first()
        if existing_username:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")
        
        new_user = UserDB(
            fullname = user.fullname,
            email = user.email,
            username = user.username,
            password = user.password,
            gender = user.gender.value
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        user_payload = {
            "id": new_user.id,
            "fullName": new_user.fullname,
            "email": new_user.email,
            "username": new_user.username,
        }
        
        return {
            "message": "User added successfully :)",
            "data": user_payload,
        }
        
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": "Exception occurred!", "detail": str(e)},
        )