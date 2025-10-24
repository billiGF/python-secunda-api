from .base import CRUDBase
from sqlalchemy import select
from src.models.building import Building
from sqlalchemy.ext.asyncio import AsyncSession



class BUILDINGCrud(CRUDBase):
    async def get_building_by_id(
            self,
            building_id,
            session: AsyncSession
        ):
        info = await session.execute(select(self.model).where(
            self.model.id == building_id
        ))
        info = info.scalars().all()
        return info



building_crud = BUILDINGCrud(Building)