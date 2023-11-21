from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from db.models import DrinkModel
from routers.schemas import DrinkBase  # Assuming you have a DrinkBase schema similar to FoodBase

def create_drink(db: Session, request: DrinkBase) -> DrinkModel:
    new_drink = DrinkModel(
        title=request.title,
        desc=request.desc,
        price=request.price,
        cover=request.cover,
        prepare_time=request.prepare_time,
        size=request.size,
        is_liked=False,
        nightspot_id=request.nightspot_id,  # Assuming this field exists in DrinkModel
    )
    db.add(new_drink)
    db.commit()
    db.refresh(new_drink)
    return new_drink

def read_drinks(db: Session, limit: int, search: str) -> list[DrinkModel]:
    return db.query(DrinkModel).filter(DrinkModel.title.contains(search)).limit(limit).all()

def read_drink(db: Session, id: int) -> DrinkModel:
    drink = db.query(DrinkModel).filter(DrinkModel.id == id).first()
    if not drink:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='There\'s no such drink with this id.')
    return drink

def delete_drink(db: Session, id: int) -> dict:
    drink = db.query(DrinkModel).filter(DrinkModel.id == id).first()
    if not drink:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='There\'s no such drink with this id.')
    db.delete(drink)
    db.commit()
    return {'results': 'deleted successfully.'}
