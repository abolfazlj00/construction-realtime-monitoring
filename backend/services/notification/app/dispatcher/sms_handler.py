from .base import HandlerInterface
from ..models.notification_message.sms.message import SMSNotificationMessage
from ..utils.log import Log

class SMSHandler(HandlerInterface[SMSNotificationMessage]):

    @classmethod
    async def handle(cls, message: SMSNotificationMessage) -> None:
        # TODO: integrate actual SMS provider later
        Log.info(f"[SMSHandler] Sending SMS to {message.data.phone}: {message.data.message}")
