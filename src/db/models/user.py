import sqlalchemy
from sqlalchemy.orm import relationship, mapped_column, Mapped
from db.base import Base
from db.types import str_128
from uuid import uuid4
from group import Group


class User(Base):
    __tablename__ = "users"

    id: Mapped[sqlalchemy.UUID] = mapped_column(sqlalchemy.UUID(as_uuid=True), primary_key=True, default=uuid4)
    email: Mapped[str_128] = mapped_column(unique=True)
    first_name: Mapped[str_128]
    last_name: Mapped[str_128]
    global_id: Mapped[sqlalchemy.UUID] = mapped_column(index=True)

    groups_with_user: Mapped[list[Group]] = relationship(
        secondary="user__group",
        back_populates="users_in_group",
    )
