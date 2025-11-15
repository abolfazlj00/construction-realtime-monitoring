import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI

from .consumer.rabbit_consumer import RabbitConsumer
from .consumer.grpc_consumer import GrpcConsumer
from .dispatcher.dispatcher import NotificationDispatcher

from .models.consumers.rabbit import RabbitConsumerSettings
from .models.consumers.grpc import GrpcConsumerSettings
from .utils.log import Log   # assuming you placed the class in utils/log.py


@asynccontextmanager
async def lifespan(app: FastAPI):

    Log.warn("Starting up...")

    loop = asyncio.get_event_loop()

    # --------------------------
    # Initialize Consumers
    # --------------------------
    rabbit_consumer = RabbitConsumer(
        settings=RabbitConsumerSettings(
            host="rabbit",
            port=5672,
            username="guest",
            password="guest",
            queue_name="notifications",
            loop=loop,
        ),
        callback=NotificationDispatcher.dispatch,
    )

    grpc_consumer = GrpcConsumer(
        settings=GrpcConsumerSettings(
            host="0.0.0.0",
            port=50052,
            loop=loop,
        ),
        callback=NotificationDispatcher.dispatch,
    )

    # ------------------------------------------------------------------
    # START CONSUMERS WITH PROPER EXCEPTION HANDLING
    # ------------------------------------------------------------------
    rabbit_task = asyncio.create_task(rabbit_consumer.start(), name="rabbit_consumer")
    grpc_task = asyncio.create_task(grpc_consumer.start(), name="grpc_consumer")

    done, pending = await asyncio.wait(
        {grpc_task, rabbit_task},
        return_when=asyncio.FIRST_EXCEPTION
    )

    for task in done:
        if task.exception():
            exc = task.exception()
            Log.error(f"{task.get_name()} failed during startup: {exc}")

            # Cancel any pending tasks cleanly
            for p in pending:
                p.cancel()
                try:
                    await p
                except asyncio.CancelledError:
                    pass

            await rabbit_consumer.close()
            await grpc_consumer.close()

            raise RuntimeError(f"NotificationService startup failure: {exc}") from exc

    Log.success("Consumers started successfully.")

    app.state.rabbit_consumer = rabbit_consumer
    app.state.grpc_consumer = grpc_consumer

    yield 

    Log.warn("Shutting down...")

    await asyncio.gather(
        rabbit_consumer.close(),
        grpc_consumer.close()
    )

    Log.success("Shutdown complete.")



# -------------------------------------------------------------------
# FastAPI Application
# -------------------------------------------------------------------
app = FastAPI(
    title="Notification Service",
    description="Handles SMS and Email notifications through RabbitMQ and gRPC.",
    version="0.1.0",
    lifespan=lifespan
)


@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok", "service": "notification"}
