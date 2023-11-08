from typing import Optional

from pydantic import BaseModel 

# create these pydantic models(schemas)
# Hero, Ability, AbilityType, Relationship< RelationType

# Data Model
class AbilityTypeModel(BaseModel):
    id: int
    name: str 

class AbilityModel(BaseModel):
    id: int
    hero_id: int
    ability_type_id: int
    ability_type: AbilityTypeModel

class HeroModel(BaseModel):
    id: int
    name: str | None
    about_me: str | None
    biography: str | None
    image_url: str | None
    abilities: list[AbilityModel]

    def __init__(self, **data):
        super().__init__(**data)
        self.abilities = self.abilities or []

    class Config:
        from_attributes = True
