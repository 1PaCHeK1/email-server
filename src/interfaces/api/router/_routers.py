from fastapi import APIRouter

from .users import router as user_router
from .email import router as email_router


router = APIRouter()

router.include_router(user_router)
router.include_router(email_router)
