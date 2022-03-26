from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .base_class import Base  


class ProductImage(Base):
    __table_args__={'schema' :'canymanagement'}
    __tablename__ = 'ProductImage'
    
    productimage_id = Column('ProductImageId', Integer, primary_key=True)
    productimage_uuid = Column('ProductImageUUID', String(36), index=True)
    productimage_type = Column('ProductImageType', String(25))
    productimage_name = Column('ProductImageName', String(25))
    
    # product_id = Column('ProductId', Integer, ForeignKey("Product.ProductId", ondelete="CASCADE"), nullable=False)
    # products = relationship("Product", back_populates="product_images")
    
    