
from fastapi import APIRouter
#from..db import create
from ..schemas import User
import wikipedia
from ..loggings import logger


router=APIRouter(
    tags=['USER']
)

logger.info("Search here")
@router.post('/')
def search(data:User):
    
    logger.debug("#get the keyword and store it in db")
    #base=create(data)
    
    logger.debug("fetch the summary")
    result=wikipedia.summary(data)
    
    return {'Keyword':data,'Summary':result}


