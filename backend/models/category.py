from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base_class import Base  


class Category(Base):
    __table_args__={'schema' :'canymanagement'}
    __tablename__ = 'Category'
    
    category_id = Column('CategoryId', Integer, primary_key=True)
    category_uuid = Column('CategoryUUID', String(36), index=True)
    category_name = Column('CategoryName', String(100), nullable=False, index=True)
    category_description = Column('CategoryDescription', String(256))
    category_image = Column('CategoryImage', String(100), nullable=False)
    
    # subcategories = relationship(
    #     "SubCategory",
    #     cascade="all, delete-orphan",
    #     back_populates = "categories",
    #     uselist = True
    # )
    
    