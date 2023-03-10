from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    Keyword:str
    


class Login(BaseModel):
   email=str
   password=str
   


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None