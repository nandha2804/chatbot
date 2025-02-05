@router.get("/suppliers/")
def get_suppliers(category: str, db: Session = Depends(get_db)):
    return crud.get_suppliers_by_category(db, category)
