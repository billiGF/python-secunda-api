from pydantic import BaseModel


class OrganizationBase(BaseModel):
    name: str
    phone_number: int
    building_id: int


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationRM(OrganizationBase):
    id: int

    class Config:
        from_attributes=True