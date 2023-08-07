from aioinject.ext.fastapi import InjectMiddleware
from fastapi import FastAPI
from core.di import create_container
from .router import router


def create_app() -> FastAPI:
    app = FastAPI()

    container = create_container()
    app.add_middleware(InjectMiddleware, container=container)

    app.include_router(router)

    return app
