from aioinject import inject
from ....core.domain.email.services import EmailService
from fastapi import APIRouter
from typing import Annotated
from aioinject import Inject
from aioinject.ext.fastapi import inject
from ..schemas import EmailMessageSchema


router = APIRouter(prefix="/email")
@router.post("/send")
@inject
async def send(
    body: EmailMessageSchema,
    emailservice: Annotated[EmailService, Inject]
) -> None:
    emailservice.send_email(body.recipients, body.title, body.message)