from fastapi import FastAPI
import httpx
import os
from pydantic import BaseModel

app = FastAPI()
STOCK_URL = os.getenv("StockService__BaseUrl")
PRODUCTS_URL = os.getenv("ProductsService__BaseUrl")

class StockAction(BaseModel):
    sku: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    sku: str
    min_stock: int

@app.get("/api/products")
async def gateway_get_products():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{PRODUCTS_URL}/products")
        return res.json()

@app.post("/api/products")
async def gateway_create_product(product: ProductCreate):
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{PRODUCTS_URL}/products", json=product.model_dump())
        return res.json()

@app.post("/api/stock/receive")
async def gateway_receive(action: StockAction):
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{STOCK_URL}/stock/receive", json=action.model_dump())
        return res.json()