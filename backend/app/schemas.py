from typing import Optional, List
from pydantic import EmailStr
from sqlmodel import SQLModel
from datetime import datetime

# User
class UserCreate(SQLModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class UserRead(SQLModel):
    id: int
    email: EmailStr
    full_name: Optional[str]
    is_active: bool
    is_superuser: bool
    created_at: datetime

# Product
class ProductCreate(SQLModel):
    name: str
    description: Optional[str] = None
    price: float
    currency: Optional[str] = "USD"
    stock: int = 0
    image_url: Optional[str] = None

class ProductRead(SQLModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    currency: str
    stock: int
    image_url: Optional[str]
    created_at: datetime

# Order
class OrderItemCreate(SQLModel):
    product_id: int
    quantity: int

class OrderCreate(SQLModel):
    user_id: int
    items: List[OrderItemCreate]

class OrderRead(SQLModel):
    id: int
    user_id: int
    total: float
    status: str
    created_at: datetime
