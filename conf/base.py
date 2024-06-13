from pathlib import Path
from typing import TYPE_CHECKING

import tomllib

if TYPE_CHECKING:
    from shared.types import EnvChoices


with open("pyproject.toml", mode="rb") as stream:
    pyproject = tomllib.load(stream)["tool"]["poetry"]


class BaseSettings:
    BASE_DIR = Path(__file__).parent.parent.parent

    ENVIRONMENT_PREFIX = "AUTH_MS"

    APP_NAME: str = pyproject["name"]
    APP_DESCRIPTION: str = pyproject["description"]
    APP_VERSION: str = pyproject["version"]

    API_PREFIX = "/api"
    DOCS_URL = "/docs"
    REDOC_URL = None
    OPENAPI_URL = "/openapi.json"

    # NOTE: These are here only for type checking purposes. They should be set in the
    # subclasses.
    if TYPE_CHECKING:
        ENVIRONMENT: "EnvChoices"
        DATABASE_URL: str
        ALLOWED_HOSTS: list[str]
        ALLOWED_ORIGINS: list[str]
        DEBUG: bool

    @classmethod
    def get_asgi_settings(cls):
        return {
            "title": cls.APP_NAME,
            "description": cls.APP_DESCRIPTION,
            "version": cls.APP_VERSION,
            "debug": cls.DEBUG,
            "docs_url": cls.DOCS_URL,
            "openapi_url": cls.OPENAPI_URL,
            "redoc_url": cls.REDOC_URL,
        }
