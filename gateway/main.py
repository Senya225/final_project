from fastapi import FastAPI
import httpx
import os

app = FastAPI()

@app.get("/api/stock")
async def gateway_stock():
    stock_url = os.getenv("StockService__BaseUrl", "http://localhost:5002")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{stock_url}/stock")
        return response.json()
