
import uuid
from sqlalchemy.orm import relationship, mapped_column, Mapped
from db.base import Base
from db.types import str_128, uuid_pk
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy
from .group import Group, UserGroup


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid_pk]
    email: Mapped[str_128] = mapped_column(unique=True)
    first_name: Mapped[str_128]
    last_name: Mapped[str_128]
    global_id: Mapped[uuid.UUID] = mapped_column(index=True)

    group_associations: Mapped[list[UserGroup]] = relationship()
    groups: AssociationProxy[list[Group]] = association_proxy(
        "group_associations",
        "group",
    )
