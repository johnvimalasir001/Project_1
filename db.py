from pymongo import MongoClient

cluster=("mongodb+srv://Johnvimalasir:Johnvimalasir@cluster0.pzm5btm.mongodb.net/Search_Details?retryWrites=true&w=majority")
client=MongoClient(cluster)

db=client()
collection=db["Details"]

def create (data):
    data = dict(data)
    response=collection.insert_one(data)
    return str(response.inserted_id)

def all():
    respopnse =collection.find({})
    return list(respopnse)

def get_one(condtion):
    response =collection.find_one({"Keyword":condtion})
    return response









