from fastapi import APIRouter
from .auth_routes import auth_router
from .order_routes import order_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(order_router)
