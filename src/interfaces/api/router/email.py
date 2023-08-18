import aio_pika
from core.domain.email.dto import EmailMessageDto
from fastapi import APIRouter
from typing import Annotated
from aioinject import Inject
from aioinject.ext.fastapi import inject
from interfaces.api.schemas.schemas import EmailMessageSchema


router = APIRouter(prefix="/email")


@router.post("/send")
@inject
async def send(
    body: EmailMessageSchema,
    rabbit_channel: Annotated[aio_pika.abc.AbstractChannel, Inject],
) -> None:
    message = EmailMessageDto(
        recipients=body.recipients,
        subject=body.title,
        message=body.message,
    )
    json_message = message.model_dump_json()

    await rabbit_channel.default_exchange.publish(
        aio_pika.Message(json_message.encode()),
        routing_key="test_queue",
    )
