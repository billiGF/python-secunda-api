from src.core.db import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .organization import Organization

class Building(Base):
    name = Column(String(50))
    address = Column(String(50))
    longitude = Column(Integer)
    latitude = Column(Integer)
    organization_id = relationship(Organization, cascade='delete')