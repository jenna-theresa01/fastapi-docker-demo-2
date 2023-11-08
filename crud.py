from sqlalchemy.orm import Session, aliased, joinedload
from models import Hero, Ability, AbilityType, relationship, RelationshipTypes
from schemas import HeroModel

def get_heroes_v1(db: Session):
    # set variable to store the query info
    heroes_query = (
        db.query(Hero).all()
    )
    # hero_models = list(heroes_query.values())
    return heroes_query

def get_heroes(db: Session):
    # set variable to store the query info
    heroes_query = (
        db.query(Hero)
        .options(joinedload(Hero.abilities).joinedload(Ability.ability_types))
        .all()
    )


    return heroes_query