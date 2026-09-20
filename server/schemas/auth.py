from enum import Enum
from pydantic import BaseModel

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHERS = "others"

class UserSignup(BaseModel):
    fullname: str
    email: str
    username: str
    gender: Gender = "male"
    password: str