from fastapi import APIRouter
from typing import Annotated
from interfaces.api.schemas.schemas import UserSchema
from aioinject import Inject
from aioinject.ext.fastapi import inject
from core.domain.user import GetUsers

router = APIRouter(prefix="/users")


@router.get("/all")
@inject
async def get_all_users(
    get_users: Annotated[GetUsers, Inject],
) -> list[UserSchema]:
    users_db = await get_users()
    users = [UserSchema(
        id=user.id,
        email=user.email,
        groups=user.groups_with_user,
    ) for user in users_db]
    return users
