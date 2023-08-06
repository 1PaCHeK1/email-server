from aioinject import inject
from fastapi import APIRouter
from typing import Annotated
from ..schemas import UserSchema
from aioinject import Inject
from sqlalchemy.orm import Session
from aioinject.ext.fastapi import inject


router = APIRouter(prefix="/users")

@router.get("/all")
@inject
async def get_all_users(
    session: Annotated[Session, Inject],
) -> list[UserSchema]:
    ...