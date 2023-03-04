from fastapi import APIRouter
from ..controllers import new_table_controller

router = APIRouter()

router.include_router(new_table_controller.router)
