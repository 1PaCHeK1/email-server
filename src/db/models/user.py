from sqlalchemy.orm import relationship, mapped_column, Mapped
from db.base import Base
from db.types import str_128, uuid
from group import Group


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid]
    email: Mapped[str_128] = mapped_column(unique=True)
    first_name: Mapped[str_128]
    last_name: Mapped[str_128]
    global_id: Mapped[uuid] = mapped_column(index=True)

    groups_with_user: Mapped[list[Group]] = relationship(
        secondary="user__group",
        back_populates="users_in_group",
    )
