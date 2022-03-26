from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType

from .base_class import Base

class Order(Base):
    __table_args__={'schema' :'canymanagement'}
    __tablename__ = 'Order'
    
    order_id = Column('OrderId', Integer, primary_key=True)
    order_uuid = Column('OrderUUID', String(36), index=True)
    order_no = Column('OrderNo', String(30), nullable=False)
    products_id = Column('ProductId', MutableList.as_mutable(PickleType), default=[], nullable=False)
    total_amount = Column('TotalAmount', Integer, nullable=False)
    # user_info_id = Column('UserInfoId', Integer, ForeignKey("UserInformation.UserInfoId", ondelete="CASCADE"), nullable=False)
