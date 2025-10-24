from fastapi import APIRouter, Depends
from src.shcemas.building import BuildingCreate, BuildingResponse, BuildingRM
from src.core.db import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.building import building_crud
from src.api.validators import cheking_building_exist



router = APIRouter()



@router.post('/')
async def create_building(
    building_form: BuildingCreate,
    session: AsyncSession = Depends(async_session)
):
   info = await building_crud.create(
      building_form, session
   )
   return info



@router.get('/', response_model=list[BuildingResponse])
async def get_all_building(
   session: AsyncSession = Depends(async_session)
):
   info = await building_crud.get(session)
   return info



@router.get('/{building_id}')
async def building_info(
   building_id: int,
   session: AsyncSession = Depends(async_session)
):
   info = await cheking_building_exist(
      building_id, session
   )
   return info