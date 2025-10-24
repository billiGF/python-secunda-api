from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select



class CRUDBase:
    def __init__(self, model):
        self.model = model


    async def create(
            self,
            creating_form,
            session: AsyncSession
        ):
        building = creating_form.dict()
        info = self.model(**building)
        session.add(info)
        await session.commit()
        await session.refresh(info)
        return info 
    

    async def get(
            self,
            session: AsyncSession,            
        ):
        info = await session.execute(select(self.model))
        info = info.scalars().all()
        return info