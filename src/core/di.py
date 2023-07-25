import smtplib
import aioinject
from functools import lru_cache

from core.domain.email.commands import SendEmailMessage
from settings import DatabaseSettings, SmtpSettings
from core.domain.email.services import EmailService, create_smtp_client
from typing import Callable, TypeVar


TSettings = TypeVar("TSettings")

def _settings_factory(type_: type[TSettings]) -> Callable[[], TSettings]:
    def inner() -> TSettings:
        return type_()

    return inner


@lru_cache
def create_container() -> aioinject.Container:
    container = aioinject.Container()

    for settings_type in (DatabaseSettings, SmtpSettings):
        container.register(
            aioinject.Singleton(_settings_factory(settings_type), type_=settings_type),
        )

    container.register(aioinject.Singleton(create_smtp_client, type_=smtplib.SMTP))
    container.register(aioinject.Callable(EmailService))
    container.register(aioinject.Callable(SendEmailMessage))

    return container
