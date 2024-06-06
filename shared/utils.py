from datetime import datetime, timezone
from functools import lru_cache
from typing import Literal, overload

from environs import Env


@lru_cache(maxsize=1)
def get_env():
    env = Env()
    env.read_env()
    return env


@overload
def utc_timestamp(unix: Literal[True] = True) -> int: ...


@overload
def utc_timestamp(unix: Literal[False] = False) -> datetime: ...


def utc_timestamp(unix: bool = False):
    utc_now = datetime.now(timezone.utc)
    if unix:
        utc_now = int(utc_now.timestamp())
    return utc_now
