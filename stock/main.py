from fastapi import FastAPI
import httpx
import os
from pydantic import BaseModel

app = FastAPI()
PRODUCTS_URL = os.getenv("ProductsService__BaseUrl")
NOTIF_URL = os.getenv("NotificationsService__BaseUrl")

class StockAction(BaseModel):
    sku: str
    quantity: int

@app.post("/stock/receive")
async def receive_stock(action: StockAction):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{PRODUCTS_URL}/products")
        products = res.json()
        product = next((p for p in products if p["sku"] == action.sku), None)
        
        if not product:
            return {"error": "Товар не найден"}
        
        message = f"Принят товар {product['name']} в количестве {action.quantity} шт."
        await client.post(f"{NOTIF_URL}/notify", json={"message": message})
        return {"status": "success", "message": message}