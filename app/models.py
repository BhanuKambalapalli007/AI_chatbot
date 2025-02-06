from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_info = Column(String)
    categories = Column(String)

    products = relationship("Product", back_populates="supplier")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand = Column(String)
    price = Column(Integer)
    category = Column(String)
    description = Column(String)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))

    supplier = relationship("Supplier", back_populates="products")
