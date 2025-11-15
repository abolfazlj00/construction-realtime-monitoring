
from ..models.notification_message.email.message import EmailNotificationMessage
from ..models.notification_message.sms.message import SMSNotificationMessage
from ..models.notification_message.union import NotificationMessage

from .base import HandlerInterface
from .email_handler import EmailHandler
from .sms_handler import SMSHandler


HANDLER_REGISTRY: dict[type[NotificationMessage], type[HandlerInterface]] = {
    EmailNotificationMessage: EmailHandler,
    SMSNotificationMessage: SMSHandler,
}
