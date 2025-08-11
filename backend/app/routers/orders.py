from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..deps import get_db, get_current_user
from ..schemas import OrderCreate, OrderRead
from .. import crud
from ..models import Order

router = APIRouter(prefix="/api/orders", tags=["orders"])

@router.post("/", response_model=OrderRead)
def create_order(order_in: OrderCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    if current_user.id != order_in.user_id and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not allowed")
    order = crud.create_order(db, order_in)
    return order

@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if order.user_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not allowed")
    return order
