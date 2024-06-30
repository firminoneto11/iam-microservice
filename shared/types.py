from typing import Literal, Protocol

from fastapi import FastAPI
from starlette.datastructures import State

type EnvChoices = Literal["development", "testing", "staging", "production"]


class _ApplicationMountProtocol(Protocol):
    path: str
    app: FastAPI
    name: str


class _CustomAppState(State):
    mounted_applications: list[_ApplicationMountProtocol]


class ASGIApp(FastAPI):
    state: _CustomAppState
