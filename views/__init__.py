from fastapi import APIRouter
from views import diagrams
from config import PREFIX


router = APIRouter(prefix=PREFIX)

router.include_router(diagrams.router)
