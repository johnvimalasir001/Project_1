from pymongo import MongoClient
#from .router import user

cluster='mongodb+srv://Johnvimalasir:vrqj3Nl90X0BYcV5@cluster0.pzm5btm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client=MongoClient(cluster)

db=client.Search_Details
collection=db.Details

def create (data):
    data = dict(data)
    response=collection.insert_one(data)
    return str(response.inserted_id)


def insert (result):
    result=dict(result)
    response=collection.insert_one(result)
    return str(response.inserted_id)



def all():
    respopnse =collection.find({})
    return list[respopnse]

def get_one(Keyword):
    response =collection.find_one(Keyword)
    return str(response)









