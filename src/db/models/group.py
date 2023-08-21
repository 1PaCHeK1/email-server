from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship, mapped_column, Mapped
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

    users_in_group: Mapped[list[User]] = relationship(
        secondary="user__group",
        back_populates="groups_with_user",
    )


class UserGroup(Base):
    __tablename__ = "user__group"

    user_id: Mapped[uuid_pk] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
    )
    group_id: Mapped[uuid_pk] = mapped_column(
        ForeignKey("groups.id", ondelete="CASCADE"),
    )

    user: Mapped[User] = relationship()
    group: Mapped[Group] = relationship()
