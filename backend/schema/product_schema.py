from fastapi_camelcase import CamelModel

class ProductBase(CamelModel):
    product_name: str
    product_mrp: int
    discount_percentage: str
    
class Products(ProductBase):
    product_description : str
    product_image: str
    
class ProductCreate(ProductBase):
    product_description : str

class ProductUpdate(ProductCreate):
    pass