import smtplib
import aioinject
import aio_pika.abc
from functools import lru_cache

from core.domain.email.commands import SendEmailMessage
from settings import DatabaseSettings, SmtpSettings, RabbitSettings
from core.domain.email.services import EmailService, create_smtp_client
import typing
from interfaces.rabbit.connection import create_connection
from interfaces.rabbit.publisher import create_channel
from sqlalchemy.orm import Session
from db.base import Database, get_session

TSettings = typing.TypeVar("TSettings")


def _settings_factory(type_: type[TSettings]) -> typing.Callable[[], TSettings]:
    def inner() -> TSettings:
        return type_()

    return inner


@lru_cache
def create_container() -> aioinject.Container:
    container = aioinject.Container()

    for settings_type in (DatabaseSettings, SmtpSettings, RabbitSettings):
        container.register(
            aioinject.Singleton(
                _settings_factory(settings_type),  # type: ignore[arg-type]
                type_=settings_type,
            ),
        )
    container.register(aioinject.Callable(get_session, Session))
    
    container.register(aioinject.Singleton(create_smtp_client, type_=smtplib.SMTP))
    container.register(
        aioinject.Singleton(create_connection, type_=aio_pika.abc.AbstractConnection),
    )
    container.register(
        aioinject.Callable(create_channel, type_=aio_pika.abc.AbstractChannel),
    )

    container.register(aioinject.Callable(EmailService))
    container.register(aioinject.Callable(SendEmailMessage))

    return container
