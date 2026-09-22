from fastapi import status, APIRouter, HTTPException, Depends
from models.document import Docs as DocumentsDataBase
from models.users import User as UserDB
from schemas.document import Document as DocumentSchema
from core.database import db_dependencies
from core.config import get_current_user

uploadeddocument = APIRouter(prefix='/document', tags=['Documents'])

@uploadeddocument.post("/get-docs-details", status_code=status.HTTP_200_OK)
def fetch_document(db: db_dependencies, docs: DocumentSchema, current_userid: str = Depends(get_current_user)):
    try:
        user = db.query(UserDB).filter(UserDB.id == int(current_userid)).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        document = DocumentsDataBase(
            userid=user.id,
            filename=docs.filename,
            filetype=docs.filetype,
            fullcontent=docs.fullcontent
        )
        db.add(document)
        db.commit()
        db.refresh(document)
        return {
            "message": "Document uploaded successfully :)",
            "data": document
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": "Exception occurred!", "detail": str(e)},
        )