from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base_class import Base  
from .category import Category


class SubCategory(Base):
    __table_args__ = {'schema' :'canymanagement'}
    __tablename__ = 'SubCategory'
    
    subcategory_id = Column('SubCategoryId', Integer, primary_key=True)
    subcategory_uuid = Column('SubCategoryUUID', String(36), index=True)
    subcategory_name = Column('SubCategoryName', String(150), nullable=False, index=True)
    subcategory_description = Column('SubCategoryDescription', String(256))
    subcategory_image = Column('SubCategoryImage', String(256), nullable=False)
    
    category_id = Column('CategoryId', Integer, ForeignKey(Category.category_id, ondelete="CASCADE"), nullable=False)
    # categories = relationship("Category", back_populates="subcategories")
    