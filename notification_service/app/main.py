from fastapi import FastAPI

from app.service import process_one_message_to_all_users


app = FastAPI()


@app.post("/send_notifications")
async def send_notifications():
    return await process_one_message_to_all_users()
