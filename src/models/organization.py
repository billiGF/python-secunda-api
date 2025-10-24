from src.core.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey



class Organization(Base):
    name = Column(String)
    phone_number = Column(Integer)
    building_id = Column(Integer, ForeignKey('building.id'))