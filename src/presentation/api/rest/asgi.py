from contextlib import asynccontextmanager
from typing import cast

from fastapi import FastAPI

from conf import settings
from shared.types import ASGIApp

from .middleware import (
    allowed_hosts_middleware_configuration,
    cors_middleware_configuration,
)
from .routers import get_routers


@asynccontextmanager
async def lifespan(app: FastAPI): ...


def get_asgi_application():
    kwargs = settings.get_asgi_settings()
    kwargs["docs_url"] = None
    kwargs["openapi_url"] = None
    kwargs["redoc_url"] = None

    application = FastAPI(**kwargs, lifespan=lifespan)

    application.add_middleware(**allowed_hosts_middleware_configuration)
    application.add_middleware(**cors_middleware_configuration)

    # TODO: Check if the middleware is drilled down into the mounted apps

    application.state._mounted_applications = []
    for router in get_routers():
        application.mount(path=router.path, app=router.app, name=router.name)
        application.state._mounted_applications.append(router)

    return cast(ASGIApp, application)


app = get_asgi_application()
