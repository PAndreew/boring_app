from sqlalchemy.orm import Session
from .models import OrderModel

def get_user_order_history(db: Session, user_id: int):
    return db.query(OrderModel).filter(OrderModel.user_id == user_id).all()
