from src.core.db import Base
from sqlalchemy.orm import relationship
from .organization import Organization
from sqlalchemy import Table ,Column, String, Integer, ForeignKey



class Building(Base):
    name = Column(String(50))
    address = Column(String(50))
    longitude = Column(Integer)
    latitude = Column(Integer)
    organization_id = relationship(Organization, cascade='delete')



from .organization import Organization
from .activities import Activities


# organization_activity = Table(
#     "organization_activity",
#     Base.metadata,
#     Column(Integer, ForeignKey('activities.id')),
#     Column(Integer, ForeignKey('organization.id'))
# )