from sqlalchemy import Column, Integer, String, ForeignKey
from src.core.db import Base


class Organization(Base):
    name = Column(String)
    number = Column(Integer)
    building_id = Column(Integer, ForeignKey('building.id'))