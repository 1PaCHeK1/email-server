from datetime import datetime
import sqlalchemy
from sqlalchemy.orm import mapped_column, Mapped
from db.base import Base
from db.types import str_128, text
from uuid import uuid4


class SendedEmails(Base):
    __tablename__ = "sendedemails"

    id: Mapped[sqlalchemy.UUID] = mapped_column(sqlalchemy.UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str_128]
    message: Mapped[text]
    sended_at: Mapped[datetime] = mapped_column(insert_default=datetime.utcnow())
    recipients: list[str]
