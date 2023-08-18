from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Text
from sqlalchemy import UUID
from uuid import uuid4

from typing import Annotated

str_128 = Annotated[str, mapped_column(String(128))]
text = Annotated[str, mapped_column(Text)]
uuid_pk = Annotated[UUID, mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)]
