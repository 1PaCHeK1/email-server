import smtplib
from collections.abc import Sequence
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from sqlalchemy.ext.asyncio import AsyncSession

from common.collections_tools import batched
from core.domain.email.dto import EmailMessageDto
from db.models import SendedEmail
from settings import SmtpSettings



def create_smtp_client(settings: SmtpSettings) -> smtplib.SMTP:
    client = smtplib.SMTP_SSL(f"{settings.host}:{settings.port}")
    client.login(settings.email, settings.password)
    return client


class SmtpService:
    def __init__(
        self,
        client: smtplib.SMTP,
        settings: SmtpSettings
    ) -> None:
        self._client = client
        self._settings = settings

    def send_email(
        self,
        recipients: Sequence[str],
        subject: str,
        message: str,
    ) -> None:
        for chunk in batched(recipients, size=self._settings.max_recipients):
            msg = MIMEMultipart()
            msg["Subject"] = subject
            msg["From"] = self._settings.email
            msg["Bcc"] = ",".join(chunk)
            msg.attach(MIMEText(message))

            self._client.send_message(msg)


class EmailService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def record(self, message: EmailMessageDto) -> SendedEmail:
        db_message = SendedEmail(
            title=message.subject,
            message=message.message,
            recipients=message.recipients,
        )
        self.session.add(db_message)
        await self.session.flush()
        return db_message