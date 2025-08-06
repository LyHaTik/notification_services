import httpx

from .base import BaseNotifier


class SMSNotifier(BaseNotifier):
    async def send(self, user: dict, message: str) -> bool:
        phone = user.get("phone")
        if not phone:
            return "У пользователя нет телефона", False
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post("https://sms-api.example.com/send", json={
                    "to": phone,
                    "text": message
                })
            return None, response.status_code == 200
        except Exception as e:
            return f"SMS error: {e}", False
