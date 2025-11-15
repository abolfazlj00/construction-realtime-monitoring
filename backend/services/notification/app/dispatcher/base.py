from typing import Protocol, TypeVar
from ..models.notification_message.message_base import BaseNotificationMessage

T = TypeVar("T", bound=BaseNotificationMessage)
class HandlerInterface[T](Protocol):

    @classmethod
    async def handle(cls, message: T) -> None: ...
