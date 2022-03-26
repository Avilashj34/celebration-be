from sqlalchemy.orm import Session
from backend.schema.category_schema import CategoryCreate
from backend.models.category import Category
from uuid import uuid4

class CategoryRepo(object):
    def create_category(self, db: Session, category: CategoryCreate):
        category = Category(category_uuid = uuid4(),
                            category_name = category.category_name,
                            category_description = category.category_description,
                            category_image = category.category_image)
        
        db.add(category)
        db.commit()
        return dict(Message = 'Category Created')
    
    def get_categories(self, db: Session):
        return db.query(Category).all()
