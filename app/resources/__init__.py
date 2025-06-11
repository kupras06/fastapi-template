"""Resource Module"""

from app.core.config import Settings
from app.resources.users.router import router as users_router


def add_routers(app):
    """Add all routers to the app"""
    app.include_router(
        users_router, prefix=f"{Settings.API_V1_STR}/users", tags=["users"]
    )
