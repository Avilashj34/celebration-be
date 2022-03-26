from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base_class import Base

class ProductSubCategoryXref(Base):
    __table_args__={'schema' :'canymanagement'}
    __tablename__ = 'ProductSubCategoryXref'
    
    psc_id = Column('PscId', Integer, primary_key=True)
    psc_uuid = Column('PscUUID', String(36), index=True)
    # subcategory_id = Column('SubCategoryId', Integer, ForeignKey("SubCategory.SubCategoryId", ondelete="CASCADE"), nullable=False)
    # product_id = Column('ProductId', Integer, ForeignKey("Product.ProductId", ondelete="CASCADE"), nullable=False)
    # categories = relationship("Category", back_populates="subcategories")
    