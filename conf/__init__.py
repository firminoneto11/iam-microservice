from typing import TYPE_CHECKING as _TypeChecking

from shared.utils import get_env as _get_env

from .base import BaseSettings as _BaseSettings

if _TypeChecking:
    from shared.types import EnvChoices as _EnvChoices


with (env := _get_env()).prefixed(_BaseSettings.ENVIRONMENT_PREFIX):
    module: "_EnvChoices" = env.str("ENVIRONMENT", "development").lower().strip()


match module:
    case "development":
        from .development import Settings as _Settings
    case "testing":
        from .testing import Settings as _Settings
    case "staging":
        from .staging import Settings as _Settings
    case "production":
        from .production import Settings as _Settings
    case _:
        raise RuntimeError(f"Invalid environment: {module!r}")


settings = _Settings()
