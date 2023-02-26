from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    Keyword:str
    


class Login(BaseModel):
   email="johnvimalasir"
   password="johnvimalasir" 
   


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None