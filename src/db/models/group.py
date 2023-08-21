from __future__ import annotations
from typing import TYPE_CHECKING
import uuid
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy

from sqlalchemy import ForeignKey
from db.base import Base
from db.types import str_128, uuid_pk

if TYPE_CHECKING:
    from .user import User


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[uuid_pk]
    name: Mapped[str_128]
    code: Mapped[str_128] = mapped_column(unique=True)

    user_associations: Mapped[list[UserGroup]] = relationship()
    users: AssociationProxy[list[User]] = association_proxy(
        "user_associations",
        "user",
    )


class UserGroup(Base):
    __tablename__ = "user__group"

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    group_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("groups.id", ondelete="CASCADE"),
        primary_key=True,
    )

    user: Mapped[User] = relationship()
    group: Mapped[Group] = relationship()
