from fastapi import HTTPException
from src.crud.building import building_crud
from sqlalchemy.ext.asyncio import AsyncSession


async def cheking_building_exist(
        building_id,
        session: AsyncSession
    ): 
    info = await building_crud.get_building_by_id(
        building_id, session
        )
    if not info:
        raise HTTPException(
            status_code=404,
            detail=f'Building with {building_id}, not found'
        )
    return info