from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db.session import get_db
from backend.schema.category_schema import CategoryCreate, Categories
from backend.repository.category_repo import CategoryRepo

router = APIRouter(
    prefix='/category',
    tags=['Category'],
    responses={404: {"description": "Not found"}}
)

@router.post('/')
def create_category(category: CategoryCreate, db: Session = Depends(get_db), category_obj: CategoryRepo = Depends(CategoryRepo)):
    return category_obj.create_category(db = db, category=category)

@router.get('/', response_model= List[Categories])
def get_categories(db: Session = Depends(get_db), category_obj: CategoryRepo = Depends(CategoryRepo)):
    return category_obj.get_categories(db)