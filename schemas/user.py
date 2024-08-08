# from pydantic import BaseModel
# from typing import Optional


# class User(BaseModel):
#     id:Optional[str]
#     name:str
#     email:str
#     password:str

def user(item)-> dict:
    return {
        "id":item["id"],
        "name":item["name"],
        "email":item["email"],
        "password":["password"]
    }
