from enum import Enum


class Channel(str, Enum):
    EMAIL = "email"
    SMS = "sms"
    TELEGRAM = "telegram"