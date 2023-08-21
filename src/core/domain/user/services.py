from collections.abc import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import User


class UserService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all_users(self) -> Sequence[User]:
        return (await self.session.scalars(select(User))).all()
