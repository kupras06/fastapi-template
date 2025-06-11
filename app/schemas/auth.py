"""Auth Schemas"""

from pydantic import BaseModel


class TokenUser(BaseModel):
    """User Token Modal"""

    id: str
    email: str
