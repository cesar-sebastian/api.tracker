from app.api.dependencies.database import get_repository
from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED
from typing import List
from app.models.tracker import Tracker
from app.db.repositories.tracker import TrackerRepository

router = APIRouter()

@router.post("/create", response_model=Tracker, name="tracker:create-tracker", status_code=HTTP_201_CREATED)
async def create_tracker(
    new_tracker: Tracker = Body(..., embed=True),
    tracker_repo: TrackerRepository = Depends(get_repository(TrackerRepository))
) -> Tracker:
    tracker_created = await tracker_repo.create_tracker(new_tracker=new_tracker)
    return tracker_created
