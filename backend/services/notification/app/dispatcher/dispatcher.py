from .registry import HANDLER_REGISTRY
from ..models.notification_message.union import NotificationMessage
from ..utils.log import Log

class NotificationDispatcher:
    """
    Dispatches typed NotificationMessage objects to the correct handler.
    """
    @classmethod
    async def dispatch(cls, message: NotificationMessage) -> None:

        message_type = type(message)

        handler = HANDLER_REGISTRY.get(message_type)

        if handler is None:
            Log.error(f"[Dispatcher] Unsupported message instance: {message_type}")
            Log.error(f"[Dispatcher] No handler registered for message type: {message_type}")
            return

        # Type-safe dispatch
        return await handler.handle(message)
            
