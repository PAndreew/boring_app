from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from db.models import NightspotModel
from routers.schemas import NightspotBase


def create_nightspot(db: Session, request: NightspotBase) -> NightspotModel:
    new_nightspot = NightspotModel(
        name=request.name,
        score=request.score,
        destination=request.destination,
        cover=request.cover,
        back_drop=request.back_drop,
        info=request.info,
        open_time=request.open_time,
        close_time=request.close_time,
    )
    db.add(new_nightspot)
    db.commit()
    db.refresh(new_nightspot)
    return new_nightspot


def read_nightspots(db: Session, limit: int, search: str) -> list[NightspotModel]:
    return db.query(NightspotModel).filter(NightspotModel.name.contains(search)).limit(limit).all()


def read_nightspot(db: Session, id: int) -> NightspotModel:
    nightspot = db.query(NightspotModel).filter(
        NightspotModel.id == id).first()
    if not nightspot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='There\'s no such nightspot  with this id.')
    return nightspot


def delete_nightspot(db: Session, id: int) -> dict:
    nightspot = db.query(NightspotModel).filter(
        NightspotModel.id == id).first()
    if not nightspot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='There\'s no such nightspot with this id.')
    db.delete(nightspot)
    db.commit()
    return {'results': 'deleted successfuly.'}
