import aio_pika
from sqlalchemy import select
from core.domain.email.services import EmailService
from fastapi import APIRouter
from typing import Annotated
from aioinject import Inject
from aioinject.ext.fastapi import inject
from interfaces.api.schemas.schemas import EmailMessageSchema
from sqlalchemy.orm import Session
from db.models import User


router = APIRouter(prefix="/email")


@router.post("/send")
@inject
async def send(
    body: EmailMessageSchema,
    emailservice: Annotated[EmailService, Inject],
    session: Annotated[Session, Inject],
    rabbit_channel: Annotated[aio_pika.abc.AbstractChannel, Inject],
) -> None:
    
    stmt = select(User.email).where(User.id in body.recipients)
    emailservice.send_email(session.scalars(stmt).all(), body.title, body.message)

    await rabbit_channel.default_exchange.publish(
        aio_pika.Message("hello world".encode()),
        routing_key="test_queue",
    )
