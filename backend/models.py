from datetime import datetime
from pydantic import EmailStr
from sqlmodel import SQLModel

import common

class UserV1(SQLModel):
    """
    Base model for user data.
    """
    id: int = 0
    usernamename: str = ""
    email: EmailStr = ""
    is_active: bool = False
    is_wizard: bool = False
    last_login: datetime = None

class UserFullV1(UserV1):
    """
    Model for a full user profile.
    """
    date_joined: datetime = None
    password: str = "" # for non OAuth users
    last_password_change: datetime = None
    last_password_reset: datetime = None
    last_email_change: datetime = None
    last_username_change: datetime = None

class UsersV1(SQLModel):
    """
    Model for a list of users.
    """
    data: list[UserV1] = []
    count: int = 0
