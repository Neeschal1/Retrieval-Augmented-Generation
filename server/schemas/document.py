from enum import Enum
from pydantic import BaseModel

class FileType(str, Enum):
    PDF = "pdf"
    TXT = "txt"
    DOCS = "docs"
    OTHERS = "others"

class Document(BaseModel):
    filename: str
    filetype: FileType = "pdf"
    fullcontent: str