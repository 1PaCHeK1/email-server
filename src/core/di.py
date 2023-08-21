import smtplib
import aioinject
import aio_pika.abc
from functools import lru_cache

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from core.domain.email.commands import SendEmailMessage
from settings import DatabaseSettings, SmtpSettings, RabbitSettings
from core.domain.email.services import SmtpService, EmailService, create_smtp_client
from .domain.user import UserService, GetUsers
import typing
from interfaces.rabbit.connection import create_connection
from interfaces.rabbit.publisher import create_channel
from db.base import create_database_engine, create_sessionmaker, get_session

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

    container.register(aioinject.Singleton(create_database_engine, AsyncEngine))
    container.register(aioinject.Singleton(
        create_sessionmaker,
        async_sessionmaker[AsyncEngine]),
    )
    container.register(aioinject.Callable(get_session, AsyncSession))

    container.register(aioinject.Singleton(create_smtp_client, type_=smtplib.SMTP))
    container.register(
        aioinject.Singleton(create_connection, type_=aio_pika.abc.AbstractConnection),
    )
    container.register(
        aioinject.Callable(create_channel, type_=aio_pika.abc.AbstractChannel),
    )

    container.register(aioinject.Callable(SmtpService))
    container.register(aioinject.Callable(EmailService))
    container.register(aioinject.Callable(SendEmailMessage))

    container.register(aioinject.Callable(UserService))
    container.register(aioinject.Callable(GetUsers))

    return container
