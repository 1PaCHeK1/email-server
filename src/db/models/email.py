from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from db.base import Base
from db.types import str_128, text, uuid


class SendedEmails(Base):
    __tablename__ = "sendedemails"

    id: Mapped[uuid]
    title: Mapped[str_128]
    message: Mapped[text]
    sended_at: Mapped[datetime] = mapped_column(insert_default=datetime.utcnow())
    recipients: Mapped[list[str]]
