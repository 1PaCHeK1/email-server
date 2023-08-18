from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import quote_plus


class DatabaseSettings(BaseSettings):

    driver: str = "postgresql+asyncpg"
    host: str = "localhost"
    port: int = 5432
    username: str = "postgres"
    password: str = "postgres"
    name: str = "email-server"
    model_config = SettingsConfigDict(env_prefix="db_")

    @property
    def url(self) -> str:
        password = quote_plus(self.password)
        return f"{self.driver}://{self.username}:{password}@{self.host}:{self.port}/{self.name}"


class SmtpSettings(BaseSettings):
    host: str
    port: int

    email: str
    password: str

    max_recipients: int = 30
    timeout: int = 10

    model_config = SettingsConfigDict(env_prefix="smtp_")


class RabbitSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="rabbit_")

    host: str
    user: str
    password: str

    prefetch_count: int = 10

    @property
    def url(self) -> str:
        return f"amqp://{self.user}:{self.password}@{self.host}/"
