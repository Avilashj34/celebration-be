from fastapi import APIRouter

from .endpoint import products
from .endpoint import category

router = APIRouter()

@router.get('/')
def index():
    return {'Msg': 'Cany API'}

router.include_router(products.router)
router.include_router(category.router)

