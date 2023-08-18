import anyio.to_thread
import functools
from .dto import EmailMessageDto
from .services import SmtpService, EmailService



class SendEmailMessage:
    def __init__(
        self,
        smtp_service: SmtpService,
        email_service: EmailService
    ) -> None:
        self.smtp_service = smtp_service
        self.email_service = email_service

    async def __call__(self, dto: EmailMessageDto) -> None:
        await anyio.to_thread.run_sync(
            functools.partial(
                self.smtp_service.send_email,
                recipients=dto.recipients,
                subject=dto.subject,
                message=dto.message,
            ),
        )
        await self.email_service.record(dto)



# Endpoint
# Command / Query
# Service
# Repository