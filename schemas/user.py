from models.user import User
from bson import ObjectId

def user_schema(user) -> dict:
    return {
        "nombre": user["nombre"],
        "email": user["email"],
        "password":user["password"]
   
    }

def users_schema(users) -> list:
    return [user_schema(user) for user in users]
