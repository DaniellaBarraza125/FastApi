from fastapi import APIRouter

user = APIRouter()

@user.get ("/")
def getUsers(): 
    return {'msg':"users"}