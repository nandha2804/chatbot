from sqlalchemy.orm import Session
from models import Supplier, Product

def get_products(db: Session, brand: str = None):
    query = db.query(Product)
    if brand:
        query = query.filter(Product.brand == brand)
    return query.all()

def get_suppliers_by_category(db: Session, category: str):
    return db.query(Supplier).filter(Supplier.product_categories.ilike(f"%{category}%")).all()

def get_product_details(db: Session, product_name: str):
    return db.query(Product).filter(Product.name.ilike(f"%{product_name}%")).first()
