from dataclasses import dataclass

from fastapi import FastAPI

from conf import settings

from .admin.users import router as admin_router
from .public.misc import router as public_misc_router
from .public.users import router as public_users_router


@dataclass
class ApplicationMount:
    path: str
    app: FastAPI
    name: str


def _get_public_app_v1():
    public_app_v1 = FastAPI(**settings.get_asgi_settings())  # type: ignore

    public_app_v1.include_router(public_misc_router)
    public_app_v1.include_router(public_users_router)

    return public_app_v1


def _get_admin_app_v1():
    admin_app_v1 = FastAPI(**settings.get_asgi_settings())  # type: ignore

    admin_app_v1.include_router(admin_router)

    return admin_app_v1


def get_mounts():
    return [
        ApplicationMount(
            path=f"{settings.public_path}/v1",
            app=_get_public_app_v1(),
            name="public_v1",
        ),
        ApplicationMount(
            path=f"{settings.admin_path}/v1",
            app=_get_admin_app_v1(),
            name="admin_v1",
        ),
    ]
