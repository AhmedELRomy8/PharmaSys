"""Routers export."""

from src.routers.auth_router import router as auth_router
from src.routers.sales_router import router as sales_router
from src.routers.medicine_router import router as medicine_router

__all__ = ["auth_router", "sales_router", "medicine_router"]
