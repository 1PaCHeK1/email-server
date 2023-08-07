from core.di import create_container
from core.domain.email.commands import SendEmailMessage
from core.domain.email.dto import EmailMessageDto
from interfaces.rabbit.connection import create_connection
from settings import RabbitSettings
import json


QUEUE_NAME = "test_queue"


async def consume() -> None:
    container = create_container()

    settings = RabbitSettings()
    connection_ctx = create_connection(settings=settings)

    async with connection_ctx as connection:
        channel = await connection.channel()

        await channel.set_qos(prefetch_count=settings.prefetch_count)
        queue = await channel.declare_queue(QUEUE_NAME, durable=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with container.context() as ctx:
                    command = await ctx.resolve(SendEmailMessage)
                    async with message.process(requeue=True):
                        data = json.loads(message.body)
                        await command(EmailMessageDto.model_validate(data))


if __name__ == "__main__":
    import anyio
    import dotenv

    dotenv.load_dotenv()

    anyio.run(consume)
