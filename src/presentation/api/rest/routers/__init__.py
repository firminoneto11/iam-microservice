from dataclasses import dataclass

from fastapi import FastAPI

from conf import settings

from .cms.users import router as cms_users_router
from .public.misc import router as public_misc_router
from .public.users import router as public_users_router


@dataclass
class ApplicationMount:
    path: str
    app: FastAPI
    name: str


def get_routers():
    # Public V1 Routes
    public_app_v1 = FastAPI(**settings.get_asgi_settings())

    public_app_v1.include_router(public_misc_router)
    public_app_v1.include_router(public_users_router)

    # CMS V1 Routers
    cms_app_v1 = FastAPI(**settings.get_asgi_settings())

    cms_app_v1.include_router(cms_users_router)

    return [
        ApplicationMount(
            path=f"{settings.public_path}/v1", app=public_app_v1, name="public_v1"
        ),
        ApplicationMount(path=f"{settings.cms_path}/v1", app=cms_app_v1, name="cms_v1"),
    ]
