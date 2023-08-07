import aio_pika
from core.domain.email.services import EmailService
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
    emailservice: Annotated[EmailService, Inject],
    rabbit_channel: Annotated[aio_pika.abc.AbstractChannel, Inject],
) -> None:
    # emailservice.send_email(body.recipients, body.title, body.message)

    await rabbit_channel.default_exchange.publish(
        aio_pika.Message("hello world".encode()),
        routing_key="test_queue",
    )
