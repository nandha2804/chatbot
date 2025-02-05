from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, autoincrement=True)  
    name = Column(String(255), nullable=False)
    contact_info = Column(Text)
    product_categories = Column(Text)

    products = relationship("Product", back_populates="supplier", cascade="all, delete")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    brand = Column(String(255))
    price = Column(DECIMAL(10,2))
    category = Column(String(100))
    description = Column(Text)
    supplier_id = Column(Integer, ForeignKey("suppliers.id", ondelete="CASCADE"), nullable=False)

    supplier = relationship("Supplier", back_populates="products")
