from typing import TYPE_CHECKING

from shared.utils import get_env

from .base import BaseSettings

if TYPE_CHECKING:
    from shared.types import EnvChoices


with (env := get_env()).prefixed(BaseSettings.ENVIRONMENT_PREFIX):
    module: "EnvChoices" = env.str("ENVIRONMENT", "development").lower().strip()


match module:
    case "development":
        from .development import Settings as settings  # noqa
    case "testing":
        from .testing import Settings as settings  # noqa
    case "staging":
        from .staging import Settings as settings  # noqa
    case "production":
        from .production import Settings as settings  # noqa
    case _:
        raise RuntimeError(f"Invalid environment: {module!r}")
