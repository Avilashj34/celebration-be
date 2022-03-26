from sqlalchemy.orm import Session

from ..models.product import Product

def get_products_by_subcategory(db: Session, sc_id: int):
    pass

def create_products(db: Session):
    pass

def get_product_by_id(db:Session):
    pass

def get_subcategory_id_from_uuid(db:Session, sc_uid: str):
    pass