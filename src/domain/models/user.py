from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import TimeStampedBaseModel


class User(TimeStampedBaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(sa.String(length=255))
    password: Mapped[str] = mapped_column(sa.String(length=300))

    first_name: Mapped[str] = mapped_column(sa.String(50))
    last_name: Mapped[str] = mapped_column(sa.String(50))
    phone_number: Mapped[Optional[str]] = mapped_column(sa.String(16), default=None)

    confirmed_email: Mapped[bool] = mapped_column(sa.Boolean(), default=False)
