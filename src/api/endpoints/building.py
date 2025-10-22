from fastapi import APIRouter, Depends
from src.shcemas.building import BuildingCreate, BuildingResponse
from src.core.db import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.building import building_crud


router = APIRouter()


@router.post('/')
async def create_building(
    building_form: BuildingCreate,
    session: AsyncSession = Depends(async_session)
):
   info = await building_crud.create(building_form, session)
   return info


@router.get('/', response_model=list[BuildingResponse])
async def get_all_building(
   session: AsyncSession = Depends(async_session)
):
   info = await building_crud.get(session)
   return info