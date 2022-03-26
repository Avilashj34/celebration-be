from typing import Text
from unicodedata import category
from fastapi_camelcase import CamelModel

class CategoryBase(CamelModel):
    category_name : str

# TODO change category_image data-type
class CategoryCreate(CategoryBase):
    category_description: Text
    category_name: str
    category_image: str
    
class Categories(CategoryCreate):
    category_uuid : str
    
    # It will check both way categories.id and categories['id']
    class Config:
        orm_mode = True