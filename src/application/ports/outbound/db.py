from abc import ABCMeta, abstractmethod
from contextlib import _AsyncGeneratorContextManager  # type: ignore

from sqlalchemy.ext.asyncio import AsyncSession


class SqlDBPort(metaclass=ABCMeta):
    @abstractmethod
    async def connect(
        self, echo_sql: bool = False, pool_size: int = 5, max_overflow: int = 5
    ) -> None: ...

    @abstractmethod
    async def disconnect(self) -> None: ...

    @abstractmethod
    async def begin_session(self) -> _AsyncGeneratorContextManager[AsyncSession]: ...

    @abstractmethod
    async def ping(self) -> None: ...
