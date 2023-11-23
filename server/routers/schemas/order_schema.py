from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class OrderItemHistory(BaseModel):
    drink_id: int
    drink_title: str
    quantity: int
    price_per_item: float

    class Config:
        orm_mode = True

class OrderHistory(BaseModel):
    order_id: int
    order_date: datetime
    items: List[OrderItemHistory]
    total_cost: float = Field(..., description="Total cost of the order")
    status: str = Field(..., description="Current status of the order (e.g., 'preparing', 'completed', 'cancelled')")

    class Config:
        orm_mode = True
