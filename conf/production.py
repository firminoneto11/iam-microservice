from shared.utils import get_env

from .base import BaseSettings

with (env := get_env()).prefixed(BaseSettings.ENVIRONMENT_PREFIX):

    class Settings(BaseSettings):
        ENVIRONMENT = "production"
        DATABASE_URL: str = env.str("DATABASE_URL")
        ALLOWED_HOSTS: list[str] = env.list("ALLOWED_HOSTS")
        ALLOWED_ORIGINS: list[str] = env.list("ALLOWED_ORIGINS")
        DEBUG = False
