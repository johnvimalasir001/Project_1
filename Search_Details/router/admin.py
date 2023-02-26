#from fastapi import APIRouter,Depends
from fastapi import APIRouter
#from Search_Details import db
from ..schemas import User
#from Search_Details import oauth2
from ..loggings import logger

router=APIRouter(
    tags=['ADMIN']
)


logger.info("welcome admin")
@router.get('/admin/all')
def all():
    logger.debug("#print all data")
    #details=db.all()
    return {'data':'print all'}

@router.get('/admin/get_one')
def one(condition:User):
    logger.debug("#print one data")
    #one_detail=db.get_one(condition)
    return {'data':'print one'}



