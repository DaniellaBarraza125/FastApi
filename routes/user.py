from fastapi import APIRouter, HTTPException
from config.db import MONGO_DETAILS, users_collection
from schemas.user import user_schema, users_schema
from models.user import User
from bson import ObjectId

user_router = APIRouter()

@user_router.get("/")
def find_all_users():
    users = users_collection.find()
    return {'msg': users_schema(users)}

@user_router.post("/")
async def create_user(user: User):
    new_user = user.dict()
    result =  users_collection.insert_one(new_user)
    created_user =  users_collection.find_one({"_id": result.inserted_id})
    return {'msg': "Usuario creado exitosamente", 'user': user_schema(created_user)}

@user_router.get("/{id}")
def find_user(id: str):
    user = users_collection.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {'msg': user_schema(user)}

@user_router.put("/{id}")
def update_user(id: str, user: User):
    updated_user = user.dict()
    users_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": updated_user})
    return {'msg': "Usuario actualizado exitosamente", "user": updated_user}

@user_router.delete("/{id}")
def delete_user(id: str):
    result = users_collection.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        return {'msg': "Usuario eliminado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
