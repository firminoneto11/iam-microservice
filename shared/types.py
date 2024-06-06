from typing import Literal, Protocol

from fastapi import FastAPI
from starlette.datastructures import State

type EnvChoices = Literal["development", "test", "staging", "production"]


class _ApplicationMountProtocol(Protocol):
    path: str
    app: FastAPI
    name: str


class _CustomAppState(State):
    _mounted_applications: list[_ApplicationMountProtocol]


class ASGIApp(FastAPI):
    state: _CustomAppState
