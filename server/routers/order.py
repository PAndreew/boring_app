from fastapi import Depends, APIRouter
from routers.schemas import UserShow
from db import db_card
from db.database import get_db
from routers.schemas.order_schema import OrderHistorySchema
from auth.oauth2 import get_current_user, oauth2_scheme

router = APIRouter(prefix='/order', tags=['Order'])

@router.get("/users/{user_id}/order-history", response_model=List[OrderHistorySchema])
def get_order_history(user_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # Ensure the requested user_id matches the current authenticated user
    if current_user.id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to access this resource")

    orders = db_order.get_user_order_history(db, user_id)
    return orders

@router.get("/orders/new", response_model=List[OrderShow])
def get_new_orders(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # Check if the current user is an employee
    if not current_user.is_admin and current_user.role != 'employee':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

    # Logic to retrieve new orders
    new_orders = db.query(OrderModel).filter(OrderModel.status == 'new').all()
    return new_orders

@router.put("/orders/{order_id}/status/preparing")
def set_order_preparing(order_id: int, db: Session = Depends(get_db)):
    # Logic to update order status to 'preparing'

@router.put("/orders/{order_id}/status/completed")
def set_order_completed(order_id: int, db: Session = Depends(get_db)):
    # Logic to update order status to 'completed'

@router.put("/orders/{order_id}/status/cancelled")
def set_order_cancelled(order_id: int, db: Session = Depends(get_db)):
    # Logic to update order status to 'cancelled'
