from pydantic import BaseModel

class ProductBase(BaseModel):
    product_name: str
    product_mrp: int
    discount_percentage: str
    
class Products(ProductBase):
    product_description : str
    product_image: str