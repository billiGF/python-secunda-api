from typing import Optional
from pydantic import BaseModel, validator, root_validator



class BuildingBase(BaseModel):
    name: str
    address: str
    longitude: int
    latitude: int

    
class BuildingCreate(BuildingBase):
    pass


class BuildingResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes=True


class BuildingRM(BuildingBase):
    id: int

    class Config:
        from_attributes=True