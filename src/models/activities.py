from sqlalchemy import Column, String
from src.core.db import Base


class Activities(Base):
    name = Column(String)