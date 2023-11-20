import shutil
from fastapi import Depends, status, APIRouter, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from routers.schemas import DrinkShow, UserShow  # Changed from FoodShow to DrinkShow
from db import db_drink 
from db.database import get_db
from routers import schemas
from auth.oauth2 import get_current_user, oauth2_scheme

router = APIRouter(prefix='/drink', tags=['Drink'])  # Changed prefix and tag

@router.get('/')
def read_drinks(limit: int = 5, search: str = '', token=Depends(oauth2_scheme), db=Depends(get_db)):
    return db_drink.read_drinks(db, limit, search)  # Changed function name and db_drink

@router.get('/{id}')
def read_drink(id: int, token=Depends(oauth2_scheme), db=Depends(get_db)):
    return db_drink.read_drink(db, id)  

@router.post('/')
def create_drink(drink: schemas.DrinkBase, user: UserShow = Depends(get_current_user), db=Depends(get_db)):
    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only admin user can access this operation.')
    return db_drink.create_drink(db, drink)  

@router.delete('/{id}')
def delete_drink(id: int,  user: UserShow = Depends(get_current_user), db=Depends(get_db)):
    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only admin user can access this operation.')
    return db_drink.delete_drink(db, id) 
