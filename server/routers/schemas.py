from pydantic import BaseModel
from typing import List


class DrinkBase(BaseModel):
    title: str
    desc: str
    price: float
    cover: str
    prepare_time: int
    size: str
    is_liked: bool
    restaurant_id: int


class DrinkShow(DrinkBase):
    id: int

    class Config:
        orm_mode = True


class RestaurantBase(BaseModel):
    name: str
    score: float
    destination: str
    cover: str
    back_drop: str
    info: str
    open_time: str
    close_time: str
    drinks: list[DrinkShow] = []


class RestaurantList(BaseModel):
    id: int
    name: str
    cover: str
    info: str

    class Config:
        orm_mode = True


class RestaurantShow(RestaurantBase):
    id: int

    class Config:
        orm_mode = True


class CartItemBase(BaseModel):
    quantity: int
    drink_id: int
    class Config:
        orm_mode = True

class CartItemShow(CartItemBase):
    id: int
    total_price: float  # Assuming this is calculated per item

class CartBase(BaseModel):
    items: List[CartItemShow] = []
    class Config:
        orm_mode = True

class CartShow(CartBase):
    total_price: float  # Assuming this is the total price for the cart
    id: int

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr
    phone: str
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str
    profile: Optional[str]  # Profile can be optional

class UserShow(UserBase):
    id: int
    cart_id: Optional[int]  # Guests will have a cart, employees might not
    cart: Optional[CartShow]  # Only applicable for guests
    is_admin: bool  # Determines if the user is an admin

# Employee Schema
class EmployeeBase(UserBase):
    role: str  # Specific role within the establishment

class EmployeeCreate(EmployeeBase):
    password: str

class EmployeeShow(EmployeeBase):
    id: int
    nightspot_id: int  # Linking employee to a specific nightspot

# Admin Schema
class AdminBase(UserBase):
    # Additional admin-specific fields if needed

class AdminCreate(AdminBase):
    password: str

class AdminShow(AdminBase):
    id: int
    managed_nightspots: List[int]  # Assuming admins manage multiple nightspots