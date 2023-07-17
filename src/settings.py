from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    username: str = "postgres"
    password: str = "postgres"

    model_config = SettingsConfigDict(
        env_prefix="db_",
    )


class SmtpSettings(BaseSettings):
    host: str
    port: int

    from_email: str
    timeout: int = 10

    model_config = SettingsConfigDict(
        env_prefix="smtp_",
    )
