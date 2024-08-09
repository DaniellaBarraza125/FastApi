from pydantic import BaseModel
from typing import Optional


class User (BaseModel):
    nombre:str
    email:str
    password:str