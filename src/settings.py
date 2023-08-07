from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    username: str = "postgres"
    password: str = "postgres"

    model_config = SettingsConfigDict(env_prefix="db_")


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
