from fastapi import APIRouter

import common
from models import (
    UserV1,
    UsersV1,
    UserFullV1
)

router = APIRouter(prefix="/v1/users", tags=["users"])

@router.get("/", response_model=UsersV1)
async def get_users_v1():
    """
    Returns a list of users.
    """
    return UsersV1(
        data = [ UserV1(id=1, username="testuser", email="test@test.com") ],
        count = 1
    )

@router.get("/{id}", response_model=UserV1)
async def get_user_v1(id: int):
    """
    Returns a user by ID.
    """
    return UserV1(id=id, username="testuser", email="test@test.com")

@router.get("/logged_in", response_model=UsersV1)
async def get_logged_in_users_v1():
    """
    Returns a list of logged-in users.
    """
    return UsersV1(
        data = [ UserV1(id=1, username="testuser", email="test@test.com", is_active=True) ],
        count = 1
    )

@router.get("/admin/{id}", response_model=UserFullV1)
async def get_user_as_wizard_v1(id: int):
    """
    Returns a user by ID.
    """
    return UserFullV1(
        id=id,
        username="testuser",
        email="test@test.com",
        is_active=False,
        is_wizard=False,
        password="HASHED_PASSWORD",
    )
