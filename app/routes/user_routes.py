from fastapi import APIRouter, Depends

from controllers.users_controllers import create_user, login
from controllers.auth import get_current_user

router = APIRouter()

@router.post("/users")
async def create_user_route(username: str, password: str):
    return await create_user(username, password)


@router.post("/login")
async def login_route(username: str, password: str):
    return await login(username, password)
