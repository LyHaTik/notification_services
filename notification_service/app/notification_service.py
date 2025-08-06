from app.notifiers.email_notifier import EmailNotifier
from app.notifiers.sms_notifier import SMSNotifier
from app.notifiers.telegram_notifier import TelegramNotifier
from app.models import Channel


class NotificationService:
    def __init__(self):
        self.notifiers = {
            Channel.EMAIL: EmailNotifier(),
            Channel.SMS: SMSNotifier(),
            Channel.TELEGRAM: TelegramNotifier(),
        }
