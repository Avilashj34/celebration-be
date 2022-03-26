from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db.session import get_db
from backend.schema.product_schema import Products
from backend.repository import product_repo

router = APIRouter(
    prefix='/product',
    tags=['product'],
    responses={404: {"description": "Not found"}}
)


@router.get('/all/{sc_uid}', response_model = List[Products])
def get_all_product(sc_uid: str, db: Session = Depends(get_db)):
    """ 
        sc_uid: subcategory uuid
    """
    sc_id = product_repo.get_subcategory_id_from_uuid(db, sc_uid)
    if sc_id is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Category Not found")
    return product_repo.get_products_by_subcategory(db, sc_id)


def create_products(db: Session = Depends(get_db)):
    pass

@router.get('/{product_id}')
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    pass

