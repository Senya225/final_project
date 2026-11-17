from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_products():
    return [
        {"Id": 1, "Name": "Ноутбук", "Sku": "LAP-001", "MinStock": 5},
        {"Id": 2, "Name": "Мышка", "Sku": "MOU-002", "MinStock": 10}
    ]
