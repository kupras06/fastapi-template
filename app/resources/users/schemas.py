"""User Schemas"""

from pydantic import BaseModel, EmailStr, SecretStr


class UserBase(BaseModel):
    """User Base"""

    name: str
    email: EmailStr
    password: SecretStr


class UserCreate(UserBase):
    """User Create"""


class UserUpdate(UserBase):
    """User Update"""

    name: str | None = None


class User(UserBase):
    """User"""

    id: int

    class Config:
        """ORM Mode"""

        orm_mode = True
        from_attributes = True
