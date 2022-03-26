import typing
from sqlalchemy import Boolean, Column, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import as_declarative, declared_attr




@as_declarative()
class Base:
    __abstract__ = True
    # __name__: str
    
    isdeleted = Column('IsDeleted', Boolean, default = False)
    isactive = Column('IsActive', Boolean, default = True)
    created_at = Column('CreatedAt', DateTime, default=datetime.now(), nullable = False)
    updated_at = Column('UpdatedAt', DateTime)
    
    # Generate __tablename__ automatically
    # @declared_attr
    # def __tablename__(cls) -> str:
    #     return cls.__name__.capitalize()
