from fastapi import status, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models.users import User as UserDB
from schemas.auth import UserSignup as SignupSchema
from schemas.auth import UserLogin as LoginSchema
from core.database import db_dependencies
from core.hash import create_hashed_data, compare_data
from core.security import create_access_token, create_refresh_token

userrouter = APIRouter(prefix='/users', tags=['Authentications'])

# Create new user
@userrouter.post('/create-users/', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependencies, user: SignupSchema):
    try:
        user_dump_data = user.model_dump()
        existing_email = (db.query(UserDB).filter(UserDB.email == user.email).first())
        if existing_email:
            return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"message": "Email already exists."})
        
        existing_username = (db.query(UserDB).filter(UserDB.username == user.username).first())
        if existing_username:
            return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"message": "Username already exists."})

        hashed_password = create_hashed_data(user_dump_data['password'])

        new_user = UserDB(
            fullname = user.fullname,
            email = user.email,
            username = user.username,
            password = hashed_password,
            gender = user.gender.value
        )

        db.add(new_user)
        db.flush()
        
        access_token = await create_access_token({"sub": str(new_user.id)})
        refresh_token = await create_refresh_token({"sub": str(new_user.id)})
        
        db.commit()
        db.refresh(new_user)
        
        return {
            "message": "User added successfully :)",
            "data": {
                "id": new_user.id,
                "fullName": new_user.fullname,
                "email": new_user.email,
                "username": new_user.username,
            },
            "token": {
                "accessToken": access_token,
                "refreshToken": refresh_token,
            }
        }
        
    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Exception occurred!", "detail": str(e)},
        )
        

# Log in an existing account from the database
@userrouter.post("/login/", status_code=status.HTTP_200_OK)
async def login(entered_detail: LoginSchema, db: db_dependencies):
    try:
        existing_user = db.query(UserDB).filter(UserDB.email == entered_detail.email).first()

        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"message": "Email not found!"},
            )

        entered_password = entered_detail.password
        db_password = existing_user.password
        match_password = compare_data(entered_password, db_password)

        if not match_password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"message": "Invalid Credentials. Try again!"}
            )
        
        access_token = await create_access_token({"sub": str(existing_user.id)})
        refresh_token = await create_refresh_token({"sub": str(existing_user.id)})
            
        return {
            "message": "Login Successful :)",
            "user": {
                "id": existing_user.id,
                "fullName": existing_user.fullname,
                "email": existing_user.email,
                "username": existing_user.username,
            },
            "tokens": {
                "accessToken": access_token,
                "refreshToken": refresh_token
            }
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": "Exception occurred!", "detail": str(e)},
        )
