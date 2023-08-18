from collections.abc import Iterator, AsyncIterable
from contextlib import contextmanager, asynccontextmanager

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import  Session, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession
from settings import DatabaseSettings


class Base(DeclarativeBase):
    pass



class Database:
    def __init__(self, settings: DatabaseSettings) -> None:
        self._engine = create_engine(
            settings.url,
            echo=settings.echo,
        )
        self.session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    @contextmanager
    def session(self) -> Iterator[Session]:
        with self.session_factory.begin() as session:
            yield session


def create_database_engine(settings: DatabaseSettings) -> AsyncEngine:
    return create_async_engine(settings.url)


def create_sessionmaker(engine: AsyncEngine) -> async_sessionmaker[AsyncEngine]:
    return async_sessionmaker(engine)


@asynccontextmanager
async def get_session(sessionmaker: async_sessionmaker[AsyncEngine]) -> AsyncIterable[AsyncSession]:
    async with sessionmaker.begin() as session:
        yield session
