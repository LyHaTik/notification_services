import os
from telethon import TelegramClient
from .base import BaseNotifier


class TelegramNotifier(BaseNotifier):
    def __init__(self):
        self.client = TelegramClient(
            "tg_session",
            int(os.getenv("API_TG_ID")),
            os.getenv("API_TG_HASH"),
            system_version="Windows 10"
        )
        self.started = False

    async def send(self, user: dict, message: str) -> bool:
        try:
            if not self.started:
                await self.client.start()
                self.started = True
            telegram_id = user.get("telegram_id")
            if not telegram_id:
                return "У пользователя нет telegram_id", False
            await self.client.send_message(telegram_id, message)
            return None, True
        except Exception as e:
            return f"Telegram error: {e}", False
