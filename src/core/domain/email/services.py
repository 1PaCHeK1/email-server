import asyncio
from collections.abc import Sequence
from smtplib import SMTP
from settings import SmtpSettings
from common.collections import batched


class SmtpService:
    def __init__(self, settings: SmtpSettings):
        self._settings = settings
        self._smtp = SMTP(
            host=settings.host,
            port=settings.port,
        )

    async def send(
        self,
        to_addrs: Sequence[str],
        content: str,
    ) -> bool:
        for email_batch in batched(to_addrs, size=1):
            self._smtp.sendmail(
                self._settings.from_email,
                to_addrs=email_batch,
                msg=content,
            )
            await asyncio.sleep(self._settings.timeout)
