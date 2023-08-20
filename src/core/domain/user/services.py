from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import User


class UserService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    
    def get_all_users(self) -> list[User]:
        return self.session.scalars(select(User)).all()
