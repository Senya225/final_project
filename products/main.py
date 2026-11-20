from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel
import os
import time

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1234@db:5432/app")
time.sleep(3) 

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sku = Column(String, unique=True)
    min_stock = Column(Integer)

Base.metadata.create_all(bind=engine)
app = FastAPI()

class ProductCreate(BaseModel):
    name: str
    sku: str
    min_stock: int

@app.get("/products")
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products

@app.post("/products")
def create_product(product: ProductCreate):
    db = SessionLocal()
    new_product = Product(name=product.name, sku=product.sku, min_stock=product.min_stock)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    db.close()
    return new_product
