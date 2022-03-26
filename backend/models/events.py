from sqlalchemy import Column, Integer, String, Text

from .base_class import Base

class Events(Base):
    __tablename__ = 'events'
    
    event_id = Column('EventId', Integer, primary_key=True, autoincrement=True)
    event_key = Column('EventKey', String)
    event_value = Column('EventValue', Text)
    