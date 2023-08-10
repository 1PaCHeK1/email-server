import sqlalchemy
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import ForeignKey
from db.base import Base
from db.types import str_128
from uuid import uuid4
from user import User


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[sqlalchemy.UUID] = mapped_column(sqlalchemy.UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str_128]
    code: Mapped[str_128] = mapped_column(unique=True)

    users_in_group: Mapped[list[User]] = relationship(
        secondary="user__group",
        back_populates="groups_with_user",
    )


class UserGroup(Base):
    __tablename__ = "user__group"

    user_id: Mapped[sqlalchemy.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    group_id: Mapped[sqlalchemy.UUID] = mapped_column(ForeignKey("groups.id", ondelete="CASCADE"))

    user: Mapped[User] = relationship(
        User,
        primaryjoin="foreign(UserGroup.user_id) == User.id",
    )
    group: Mapped[Group] = relationship(
        Group,
        primaryjoin="foreign(UserGroup.group_id) == Group.id",
    )
    