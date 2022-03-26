from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .base_class import Base  


class Product(Base):
    __table_args__={'schema' :'canymanagement'}
    __tablename__ = 'Product'
    
    product_id = Column('ProductId', Integer, primary_key=True)
    product_uuid = Column('ProductUUID', String(36), index=True)
    product_name = Column('ProductName', String(256), nullable=False, index=True)
    product_mrp = Column('ProductMrp', Integer, nullable=False)
    discount_percentage = Column('DiscountPercentage', Integer, nullable = False)
    discount_price = Column('DiscountPrice', Integer)
    product_description = Column('ProductDescription', Text)
    
    # product_images = relationship(
    #     "ProductImage",
    #     cascade="all, delete-orphan",
    #     back_populates = "products",
    #     useList = True,
    # )
    