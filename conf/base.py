import tomllib
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shared.types import EnvChoices


with open("pyproject.toml", mode="rb") as stream:
    pyproject: dict[str, str] = tomllib.load(stream)["tool"]["poetry"]


class BaseSettings:
    BASE_DIR = Path(__file__).parent.parent

    ENVIRONMENT_PREFIX = "IAM_MS"

    APP_NAME = pyproject["name"]
    APP_DESCRIPTION = pyproject["description"]
    APP_VERSION = pyproject["version"]

    DOCS_URL = "/docs"
    REDOC_URL = None
    OPENAPI_URL = "/openapi.json"

    @property
    def PUBLIC_API(self):
        return "/api"

    @property
    def ADMIN_API(self):
        return "/admin-api"

    # NOTE: These are here only for type checking purposes. They should be set in the
    # subclasses.
    if TYPE_CHECKING:
        ENVIRONMENT: "EnvChoices"
        DATABASE_URL: str
        ALLOWED_HOSTS: list[str]
        ALLOWED_ORIGINS: list[str]
        DEBUG: bool

    @classmethod
    def get_asgi_settings(cls, main_mount: bool = False):
        return {
            "title": cls.APP_NAME,
            "description": cls.APP_DESCRIPTION,
            "version": cls.APP_VERSION,
            "debug": cls.DEBUG,
            "docs_url": None if main_mount else cls.DOCS_URL,
            "openapi_url": None if main_mount else cls.OPENAPI_URL,
            "redoc_url": None if main_mount else cls.REDOC_URL,
        }
