from db.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship


class DrinkModel(Base):
    __tablename__ = 'drinks'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    desc = Column(String(255))
    price = Column(Float(2))
    cover = Column(String)
    prepare_time = Column(Integer)
    size = Column(String(1))
    is_liked = Column(Boolean)
    stock_status = Column(Boolean, default=True)  # New field
    menu_id = Column(Integer, ForeignKey('menus.id'))

    cart_items = relationship('CartItemModel', back_populates='drink')
    menu = relationship('MenuModel', back_populates='drinks')


class WineModel(Base):
    __tablename__ = 'wines'
    id = Column(Integer, primary_key=True)
    grape_variety = Column(String)
    region = Column(String)
    vintage = Column(Integer)
    drink_id = Column(Integer, ForeignKey('drinks.id'))
    drink = relationship('DrinkModel')

class BeerModel(Base):
    __tablename__ = 'beers'
    id = Column(Integer, primary_key=True)
    brewery = Column(String)
    alcohol_content = Column(Float)
    drink_id = Column(Integer, ForeignKey('drinks.id'))
    drink = relationship('DrinkModel')

class CocktailModel(Base):
    __tablename__ = 'cocktails'
    id = Column(Integer, primary_key=True)
    ingredients = Column(String)
    drink_id = Column(Integer, ForeignKey('drinks.id'))
    drink = relationship('DrinkModel')


class SoftDrinkModel(Base):
    __tablename__ = 'soft_drinks'
    id = Column(Integer, primary_key=True)
    flavor = Column(String)  # Specific attribute for soft drinks
    sugar_free = Column(Boolean, default=False)  # Indicates if the drink is sugar-free
    drink_id = Column(Integer, ForeignKey('drinks.id'))
    
    drink = relationship('DrinkModel')  # Relationship with the base DrinkModel

class SpiritModel(Base):
    __tablename__ = 'spirits'
    id = Column(Integer, primary_key=True)
    type = Column(String)  # Type of spirit (e.g., vodka, whiskey)
    age = Column(Integer)  # Age of the spirit (if applicable)
    alcohol_content = Column(Integer)  # Alcohol percentage
    drink_id = Column(Integer, ForeignKey('drinks.id'))
    
    drink = relationship('DrinkModel')  # Relationship with the base DrinkModel

class ChampagneModel(Base):
    __tablename__ = 'champagnes'
    id = Column(Integer, primary_key=True)
    region = Column(String)  # Region where the champagne is produced
    vintage = Column(Integer)  # Year of production
    sweetness = Column(String)  # Sweetness level (e.g., Brut, Extra Brut)
    drink_id = Column(Integer, ForeignKey('drinks.id'))

    drink = relationship('DrinkModel')  # Relationship with the base DrinkModel