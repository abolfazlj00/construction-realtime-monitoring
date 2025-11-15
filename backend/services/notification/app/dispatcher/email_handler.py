from .base import HandlerInterface
from ..models.notification_message.email.message import EmailNotificationMessage
from ..utils.log import Log

class EmailHandler(HandlerInterface[EmailNotificationMessage]):
    
    @classmethod
    async def handle(cls, message: EmailNotificationMessage):
        # TODO: integrate actual email provider later
        Log.info(f"[EmailHandler] Sending EMAIL to {message.data.to}: {message.data.subject}")
