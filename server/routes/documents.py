from fastapi import status, APIRouter, HTTPException
from models.document import Docs as DocumentsDataBase
from schemas.document import Document as DocumentSchema
from core.database import db_dependencies

uploadeddocument = APIRouter(prefix='/document', tags=['Documents'])

@uploadeddocument.post("/get-docs-details", status_code=status.HTTP_200_OK)
def fetch_document(db: db_dependencies, docs: DocumentSchema):
    try:
        user_docs = docs.model_dump()
        document = DocumentsDataBase(**user_docs)
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