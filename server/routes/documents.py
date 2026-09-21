from fastapi import status, APIRouter, HTTPException
from models.document import Docs as DocumentsDataBase
from schemas.document import Document as DocumentSchema
from core.database import db_dependencies

uploadeddocument = APIRouter(prefix='/document', tags=['Documents'])

@uploadeddocument.get("/get-docs-details", status_code=status.HTTP_200_OK)
def fetch_document():
    return {"message": "Document Fetched!"}