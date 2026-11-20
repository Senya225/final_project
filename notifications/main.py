from fastapi import FastAPI
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()

class Notification(BaseModel):
    message: str

@app.post("/notify")
def send_notification(notification: Notification):
    logging.info(f"ПОЛУЧЕНО УВЕДОМЛЕНИЕ: {notification.message}")
    return {"status": "ok"}
