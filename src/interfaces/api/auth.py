from typing import Annotated
from fastapi import Depends
from fastapi.security import APIKeyHeader


_auth_strategy = APIKeyHeader(name="Authorization")


AuthToken = Annotated[str, Depends(_auth_strategy)]


class Application:
    ...


def authorization_app(
    token: AuthToken,
) -> Application:
    ...


AuthApp = Annotated[Application, Depends(authorization_app)]
