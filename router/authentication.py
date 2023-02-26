from fastapi import APIRouter,Depends,HTTPException,status

from ..Search_Details import db
from .import JWTtoken
from ..Search_Details import schemas
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(
    tags =['Authentication']
)



@router.post('/login')
def login(db: Depends(db.collection),request:OAuth2PasswordRequestForm = Depends()):
    user = db.query(schemas.Login).filter(schemas.Login.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")
        
    
    

    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}