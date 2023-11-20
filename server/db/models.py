from db.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship



class NightspotModel(Base):
    __tablename__ = 'nightspots'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    score = Column(Float(1))
    destination = Column(String(20))
    cover = Column(String(20))
    back_drop = Column(String(20))
    info = Column(String(20))
    open_time = Column(String(20))
    close_time = Column(String(20))

    employees = relationship('EmployeeModel', back_populates='nightspot')
    menus = relationship('MenuModel', back_populates='nightspot')


class CartModel(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)

    items = relationship('CartItemModel', back_populates='cart')
    user = relationship('UserModel', back_populates='cart', uselist=False)


class CartItemModel(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    food_id = Column(Integer, ForeignKey("foods.id"))

    cart = relationship('CartModel', back_populates='items')
    drink = relationship('DrinkModel', back_populates='cart_items')


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    stripe_customer_id = Column(String)  # Store Stripe customer ID
    username = Column(String)
    email = Column(String)
    profile = Column(String)
    phone = Column(String)
    is_admin = Column(Boolean)
    password = Column(String)
    cart_id = Column(Integer, ForeignKey("carts.id"))

    cart = relationship('CartModel', back_populates='user')


class EmployeeModel(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)

    # Basic Employee Information
    name = Column(String(50))
    role = Column(String(20))  # e.g., 'bartender', 'admin'
    email = Column(String(50))  # Optional: For communication or login
    
    # Link to the Nightspot they work at
    nightspot_id = Column(Integer, ForeignKey('nightspots.id'))
    
    # Indicates if the employee is currently active or not
    is_active = Column(Boolean, default=True)

    # Relationship with the NightspotModel
    nightspot = relationship('NightspotModel', back_populates='employees')


class MenuModel(Base):
    __tablename__ = 'menus'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))  # Title of the menu
    description = Column(String(255))  # Description of the menu
    nightspot_id = Column(Integer, ForeignKey('nightspots.id'))  # Link to the nightspot

    nightspot = relationship('NightspotModel', back_populates='menus')
    drinks = relationship('DrinkModel', back_populates='menu')


