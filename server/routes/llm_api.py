from fastapi import status, APIRouter, HTTPException, Depends
from models.llm import APIKey as APIKeyDB
from models.users import User as UserDB
from schemas.llm import APIKey as APIKeySchema
from core.database import db_dependencies
from core.config import get_current_user
from core.ciphertext import encrypt_data, decrypt_data

llmapi = APIRouter(prefix="/llm", tags=["Api Key"])

@llmapi.post("/register-api-key", status_code=status.HTTP_201_CREATED)
async def create_api_key ( db: db_dependencies, user_apikey: APIKeySchema, current_userid: str = Depends(get_current_user),):
    try:
        user = db.query(UserDB).filter(UserDB.id == int(current_userid)).first()
        if not user:
            raise HTTPException(status_code=404, detail={"message": "User not found"})
        
        encrypted_key = encrypt_data(user_apikey.key) 

        apikey = APIKeyDB(
            userid=user.id, 
            key=encrypted_key
        )
        
        db.add(apikey)
        db.commit()
        db.refresh(apikey)
        
        return {"message": "API Key uploaded successfully :)", "data": apikey}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": "Exception occurred!", "detail": str(e)},
        )
