from fastapi import Depends, status, APIRouter, HTTPException
from sqlalchemy.orm import Session
from routers.schemas import NightspotBase, NightspotShow, NightspotList
from db import db_nightspot  # Assuming you have a similar module for nightspot as you had for restaurant
from db.database import get_db
from routers import schemas
from auth.oauth2 import oauth2_scheme, get_current_user

router = APIRouter(prefix='/nightspot', tags=['Nightspot'])

@router.get('/', response_model=list[NightspotList])
def read_nightspots(limit: int = 5, search: str = '', token=Depends(oauth2_scheme), db=Depends(get_db)):
    return db_nightspot.read_nightspots(db, limit, search)

@router.get('/{id}', response_model=NightspotShow)
def read_nightspot(id: int, token=Depends(oauth2_scheme), db=Depends(get_db)):
    return db_nightspot.read_nightspot(db, id)

@router.post('/')
def create_nightspot(nightspot: NightspotBase, user: schemas.UserShow = Depends(get_current_user), db=Depends(get_db)):
    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only admin user can access this operation.')
    return db_nightspot.create_nightspot(db, nightspot)

@router.delete('/{id}')
def delete_nightspot(id: int, user: schemas.UserShow = Depends(get_current_user), db=Depends(get_db)):
    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only admin user can access this operation.')
    return db_nightspot.delete_nightspot(db, id)
