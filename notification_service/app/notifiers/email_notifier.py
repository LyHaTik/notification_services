import os
from aiosmtplib import send
from email.message import EmailMessage
from .base import BaseNotifier


class EmailNotifier(BaseNotifier):
    async def send(self, user: dict, message: str) -> bool:
        if not user.get("email"):
            return "У пользователя нет e-mail", False
        try:
            email = EmailMessage()
            email["From"] = os.getenv("SMTP_USER")
            email["To"] = user["email"]
            email["Subject"] = "Уведомление"
            email.set_content(message)

            await send(
                email,
                hostname=os.getenv("SMTP_HOST"),
                port=int(os.getenv("SMTP_PORT")),
                username=os.getenv("SMTP_USER"),
                password=os.getenv("SMTP_PASSWORD"),
                start_tls=True
            )
            return None, True
        except Exception as e:
            return f"Email error: {e}", False
