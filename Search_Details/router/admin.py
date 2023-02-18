from fastapi import APIRouter,Depends
from Search_Details import db
from ..schemas import User,Login
from Search_Details import oauth2

router=APIRouter(
    tags=['ADMIN']
)



@router.get('/admin/all')
def all(db:Depends(db.collection),current_user:Login =Depends(oauth2.get_current_user)):
    details=db.all()
    return details

@router.get('/admin/get_one')
def one(condition:User,current_user:Login =Depends(oauth2.get_current_user)):
    one_detail=db.get_one(condition)
    return one_detail



