import anyio.to_thread
import functools
from .dto import EmailMessageDto
from .services import EmailService



class SendEmailMessage:
    def __init__(
        self,
        service: EmailService
    ) -> None:
        self._service = service

    async def __call__(self, dto: EmailMessageDto) -> None:
        await anyio.to_thread.run_sync(
            functools.partial(
                self._service.send_email,
                recipients=dto.recipients,
                subject=dto.subject,
                message=dto.message,
            ),
        )
