from src.core.db import Base
from sqlalchemy import Column, String, Integer


class Building(Base):
    nane = Column(String(20))
    longitude = Column(Integer)
    latitude = Column(Integer)