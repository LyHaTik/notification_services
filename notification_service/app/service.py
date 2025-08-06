from app.db.connect import get_conn
from app.db.func import get_message, get_users, instert_log, update_status_message
from app.notification_service import NotificationService
from app.models import Channel


async def process_one_message_to_all_users():

    service = NotificationService()

    async with get_conn() as conn:
        message = await get_message(conn)
        if not message:
            return {"detail": "Нет сообщений для отправки."}

        users = await get_users(conn)
        for user in users:
            user_dict = dict(user)
            for channel in Channel:
                notifier = service.notifiers[channel]
                try:
                    error, success = await notifier.send(user_dict, message["message"])
                    status = "success" if success else "failure"
                except Exception as e:
                    status = "failure"
                    error = str(e)
                await instert_log(conn, user["id"], message["id"], channel, status, error)
        await update_status_message(conn, message["id"])

    return {"detail": "Сообщение разослано"}
