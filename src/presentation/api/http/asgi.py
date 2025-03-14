from contextlib import asynccontextmanager
from typing import cast

from fastapi import FastAPI

from conf import settings
from shared.types import ASGIApp
from src.infra.db import SqlDBAdapter

from .middleware import (
    allowed_hosts_middleware_configuration,
    cors_middleware_configuration,
)
from .routers import get_mounts


@asynccontextmanager
async def lifespan(app: ASGIApp):
    await app.state.db.connect()
    yield
    await app.state.db.disconnect()


class ASGIFactory:
    _apps_stack: list[ASGIApp] = []

    @classmethod
    def new(cls):
        application = cls().application
        cls._apps_stack.append(application)
        return application

    @classmethod
    def latest_app(cls):
        return cls._apps_stack[-1]

    def __init__(self):
        self.application = cast(
            ASGIApp,
            FastAPI(**settings.get_asgi_settings(main_mount=True), lifespan=lifespan),  # type: ignore
        )

        self.setup_state()
        self.register_middleware()

    def setup_state(self):
        self.application.state.db = SqlDBAdapter(settings.DATABASE_URL)
        self.application.state.mounted_applications = []

        for mount in get_mounts():
            self.application.mount(path=mount.path, app=mount.app, name=mount.name)
            self.application.state.mounted_applications.append(mount)

    def register_middleware(self):
        self.application.add_middleware(**allowed_hosts_middleware_configuration)  # type: ignore
        self.application.add_middleware(**cors_middleware_configuration)  # type: ignore


app = ASGIFactory.new()
