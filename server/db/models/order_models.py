from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime

class OrderModel(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    total_cost = Column(Float)  # Total cost of the order
    order_date = Column(DateTime, default=datetime.utcnow)  # Date and time when the order was placed
    status = Column(String)  # Order status (e.g., 'pending', 'completed', 'cancelled')
    user_id = Column(Integer, ForeignKey('users.id'))  # Link to the user who placed the order

    user = relationship('UserModel')  # Relationship to the UserModel
    order_items = relationship('OrderItemModel', back_populates='order')  # Relationship to the items in the order

class OrderItemModel(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))  # Link to the order
    drink_id = Column(Integer, ForeignKey('drinks.id'))  # Link to the drink
    quantity = Column(Integer)  # Quantity of the drink ordered

    order = relationship('OrderModel', back_populates='order_items')  # Relationship to the OrderModel
    drink = relationship('DrinkModel')  # Relationship to the DrinkModel
