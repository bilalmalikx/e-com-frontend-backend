from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..deps import get_db
from ..schemas import ProductCreate, ProductRead
from .. import crud

router = APIRouter(prefix="/api/products", tags=["products"])

@router.post("/", response_model=ProductRead)
def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    prod = crud.create_product(db, product_in)
    return prod

@router.get("/", response_model=list[ProductRead])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_products(db, skip=skip, limit=limit)

@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    prod = crud.get_product(db, product_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    return prod
