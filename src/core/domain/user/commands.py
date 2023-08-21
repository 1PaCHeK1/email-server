from .services import UserService
from collections.abc import Sequence
from db.models import User

class GetUsers:
    def __init__(self, service: UserService):
        self.service = service

    async def __call__(self) -> Sequence[User]:
        return await self.service.get_all_users()
