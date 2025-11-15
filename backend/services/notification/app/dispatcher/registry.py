from .handlers.base import HandlerInterface
from .handlers.sms import SMSHandler
from .handlers.email import EmailHandler

from .providers.base import ProviderInterface
from .providers.sms.kavenegar import KavenegarProvider
from .providers.email.smtp import SMTPProvider

from ..models.notification_message.union import NotificationMessage
from ..models.notification_message.email.message import EmailNotificationMessage
from ..models.notification_message.sms.message import SMSNotificationMessage


sms_handler = SMSHandler(
    providers=[
        KavenegarProvider(),
    ]
)

email_handler = EmailHandler(
    providers=[
        SMTPProvider(),
    ]
)

HANDLER_REGISTRY: dict[type[NotificationMessage], HandlerInterface[ProviderInterface, NotificationMessage]] = {
    EmailNotificationMessage: email_handler,
    SMSNotificationMessage: sms_handler,
}
