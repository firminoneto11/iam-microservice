from contextlib import asynccontextmanager
from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from conf import settings
from src.application.ports.outbound.db import DBPort

from .db import Database


@lru_cache(typed=True)
def _get_database(connection_string: str):
    return Database(connection_string)


class DBAdapter(DBPort):
    def __init__(self, connection_string: str):
        self._database = _get_database(connection_string)

    @property
    def database(self):
        return self._database

    async def connect(
        self, echo_sql: bool = False, pool_size: int = 5, max_overflow: int = 10
    ):
        await self.database.connect(
            echo_sql=echo_sql, pool_size=pool_size, max_overflow=max_overflow
        )

    async def disconnect(self):
        await self.database.disconnect()

    @asynccontextmanager
    async def begin_session(self):  # type: ignore
        async with self.database.begin_session() as session:
            yield session

    async def ping(self):
        await self.database.ping()


async def _db_session():
    async with _get_database(settings.DATABASE_URL).begin_session() as session:
        yield session


Session = Annotated[AsyncSession, Depends(_db_session)]
