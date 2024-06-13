import tomllib
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shared.types import EnvChoices


with open("pyproject.toml", mode="rb") as stream:
    pyproject: dict = tomllib.load(stream)["tool"]["poetry"]


class BaseSettings:
    BASE_DIR = Path(__file__).parent.parent

    ENVIRONMENT_PREFIX = "IAM_MS"

    APP_NAME: str = pyproject["name"]
    APP_DESCRIPTION: str = pyproject["description"]
    APP_VERSION: str = pyproject["version"]

    DOCS_URL = "/docs"
    REDOC_URL = None
    OPENAPI_URL = "/openapi.json"

    PUBLIC_PREFIX = "/public"
    CMS_PREFIX = "/cms"
    API_PREFIX = "/api"

    @property
    def public_path(self):
        return self.PUBLIC_PREFIX + self.API_PREFIX

    @property
    def cms_path(self):
        return self.CMS_PREFIX + self.API_PREFIX

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
