
from fastapi import APIRouter
from Search_Details import db
#from..db import create
from ..Search_Details.schemas import User
import wikipedia
from ..Search_Details.loggings import logger


router=APIRouter(
    tags=['USER']
)

logger.info("Search here")
@router.post('/')
def search(data:User):
    
    logger.debug("#get the keyword and store it in db")
    
    
    logger.debug("fetch the summary")
    result=wikipedia.summary(data)
    base=db.create(data)
    store= db.insert(result)
    
    return ({'Keyword':data,'Summary':result},base,result)


