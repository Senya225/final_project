from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Notification(BaseModel):
    message: str

@app.post("/notify")
def send_notification(notification: Notification):
    print(f"[УВЕДОМЛЕНИЕ] {notification.message}")
    return {"Status": "Отправлено"}
