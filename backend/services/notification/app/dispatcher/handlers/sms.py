from .base import HandlerInterface
from ..providers.sms.base import SMSProvider
from ...models.notification_message.sms.message import SMSNotificationMessage

class SMSHandler(HandlerInterface[SMSProvider, SMSNotificationMessage]): ...
