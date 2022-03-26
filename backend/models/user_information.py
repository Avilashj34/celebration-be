from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text

from .base_class import Base


class UserInformation(Base):
    __table_args__={'schema' :'canymanagement'}
    __tablename__ = 'UserInformation'
    
    user_info_id = Column('UserInfoId', Integer, primary_key=True)
    user_info_uuid = Column('UserInfoUUID', String(36), index=True)
    mobile_no = Column('MobileNo', String(10), nullable=False, index=True)
    full_name = Column('FullName', String(50), nullable=False) 
    address_line1 = Column('AddressLine1', Text)
    address_line2 = Column('AddressLine2', Text)
    pincode = Column('Pincode', Integer, nullable=False)
    landmark = Column('Landmark', String(50))
    whatsapp_update = Column('WhatappUpdate', Boolean, default=False)
    