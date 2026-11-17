from fastapi import FastAPI
import httpx
import os

app = FastAPI()

@app.get("/stock")
async def get_stock():
    products_url = os.getenv("ProductsService__BaseUrl", "http://localhost:5001")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{products_url}/products")
        products = response.json()
    
    return {"Message": "Данные получены от Products", "ProductsData": products}
