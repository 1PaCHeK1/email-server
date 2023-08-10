from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Text

from typing import Annotated

str_128 = Annotated[str, mapped_column(String(128))]
text = Annotated[str, mapped_column(Text)]
