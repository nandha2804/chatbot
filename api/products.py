from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud
from database import get_db

router = APIRouter()

@router.get("/products/")
def get_products(brand: str = None, db: Session = Depends(get_db)):
    return crud.get_products(db, brand)
