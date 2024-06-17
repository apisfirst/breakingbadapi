from fastapi import APIRouter
from . import characters, episodes

router = APIRouter()

# router.include_router(characters.router, prefix="/characters", tags=["characters"])
router.include_router(episodes.router, prefix="/episodes", tags=["episodes"])
