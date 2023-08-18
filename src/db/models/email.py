from datetime import datetime
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.dialects.postgresql import ARRAY
from db.base import Base
from db.types import str_128, text, uuid_pk


class SendedEmail(Base):
    __tablename__ = "sendedemails"

    id: Mapped[uuid_pk]
    title: Mapped[str_128]
    message: Mapped[text]
    sended_at: Mapped[datetime] = mapped_column(insert_default=datetime.utcnow())
    recipients: Mapped[list[str]] = mapped_column(ARRAY(String))
