from fastapi import APIRouter
from typing import Annotated
from interfaces.api.schemas.schemas import UserSchema, GroupSchema
from aioinject import Inject
from sqlalchemy.orm import Session
from aioinject.ext.fastapi import inject
from db.models import User
from sqlalchemy import select


router = APIRouter(prefix="/users")


@router.get("/all")
@inject
async def get_all_users(
    session: Annotated[Session, Inject],
) -> list[UserSchema]:
    stmt = session.scalars(select(User.id, User.email, User.groups_with_user)).all()
    users = []
    for (id, email, groups) in stmt:
        users.append(UserSchema.model_validate({
            "id": id,
            "email": email,
            "groups": [GroupSchema.model_validate({"id": group.id, "name": group.name}) for group in groups],
        }))
    return users
