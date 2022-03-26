from fastapi import APIRouter

from .endpoint import products

router = APIRouter()

router.include_router(products.router)