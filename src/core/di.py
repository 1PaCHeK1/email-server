import aioinject
from functools import lru_cache
from settings import DatabaseSettings, SmtpSettings
from core.domain.email.services import SmtpService

from typing import TypeVar

T = TypeVar("T")

def settings_factory(settings_type: type[T]) -> T:
    return settings_type()


@lru_cache
def create_container() -> aioinject.Container:
    container = aioinject.Container()

    for settings_type in (DatabaseSettings, SmtpSettings):
        container.register(aioinject.Object(settings_factory(settings_type), type_=settings_type))

    container.register(aioinject.Singleton(SmtpService))

    return container
