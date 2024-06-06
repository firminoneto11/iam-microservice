from typing import TYPE_CHECKING, Optional

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from shared.utils import generate_uuid, utc_timestamp

if TYPE_CHECKING:
    from datetime import datetime


class TimeStampedBaseModel(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        sa.BigInteger().with_variant(sa.Integer(), "sqlite"),
        primary_key=True,
        autoincrement=True,
        sort_order=-2,
    )

    uuid: Mapped[str] = mapped_column(
        sa.String(36), unique=True, default=generate_uuid, sort_order=-1
    )

    # NOTE: Subclasses fields will be placed in-between these base fields on a database
    # level.

    active: Mapped[bool] = mapped_column(sa.Boolean(), default=True, sort_order=9995)

    deleted: Mapped[bool] = mapped_column(sa.Boolean(), default=False, sort_order=9996)

    created_at: Mapped["datetime"] = mapped_column(
        sa.DateTime(timezone=True),
        default=utc_timestamp,
        sort_order=9997,
    )

    updated_at: Mapped["datetime"] = mapped_column(
        sa.DateTime(timezone=True),
        default=utc_timestamp,
        onupdate=utc_timestamp,
        sort_order=9998,
    )

    deleted_at: Mapped[Optional["datetime"]] = mapped_column(
        sa.DateTime(timezone=True), default=None, sort_order=9999
    )
