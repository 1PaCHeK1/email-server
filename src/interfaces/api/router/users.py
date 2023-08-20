from fastapi import APIRouter
from typing import Annotated
from interfaces.api.schemas.schemas import UserSchema, GroupSchema
from aioinject import Inject
from sqlalchemy.orm import Session
from aioinject.ext.fastapi import inject
from db.models import User
from sqlalchemy import select
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
