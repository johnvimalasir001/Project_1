
from fastapi import APIRouter
from..db import create
from ..schemas import User
import wikipedia


router=APIRouter(
    tags=['USER']
)


@router.post('/user/search')
def search(data:User):
    base=create(data)
    result=wikipedia.summary(data)
    return {'Keyword':data,'Summary':result}


