from app.api.dependencies.database import get_repository
from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED
from typing import List
from app.models.property import PropertyCreate, PropertyPublic
from app.db.repositories.property import PropertyRepository

router = APIRouter()

@router.post("/create", response_model=PropertyPublic, name="property:create-property", status_code=HTTP_201_CREATED)
async def create_property(
    new_property: PropertyCreate = Body(..., embed=True),
    property_repo: PropertyRepository = Depends(get_repository(PropertyRepository))
) -> PropertyPublic:
    property_created = await property_repo.create_property(new_property=new_property)
    return property_created
