from fastapi import FastAPI
from models import Hero, Ability, AbilityType, Relationship, RelationshipTypes
from sqlalchemy import select
from enum import Enum

from routes import heroes

app = FastAPI()
app.include_router(heroes.router)

@app.get("/")
async def read_root():
    return "hello world"