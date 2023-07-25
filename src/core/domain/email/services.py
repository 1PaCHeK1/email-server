import smtplib
from collections.abc import Sequence
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.collections_tools import batched
from settings import SmtpSettings



def create_smtp_client(settings: SmtpSettings) -> smtplib.SMTP:
    client = smtplib.SMTP_SSL(f"{settings.host}:{settings.port}")
    client.login(settings.email, settings.password)
    return client


class EmailService:
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
