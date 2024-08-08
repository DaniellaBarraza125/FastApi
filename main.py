from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from routes.user import user

app = FastAPI()

app.include_router(user)


