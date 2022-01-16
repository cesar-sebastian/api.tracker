from typing import List
from fastapi import APIRouter
from app.api.services.report import ReportService
from app.db.repositories.tracker import TrackerRepository
from app.db.repositories.property import PropertyRepository
from fastapi import Depends
from app.api.dependencies.database import get_repository

router = APIRouter()

@router.get("/summary-stay/{day}")
async def get_tracker_day(
        day:str,
        property_repo: PropertyRepository = Depends(get_repository(PropertyRepository)),
        tracker_repo: TrackerRepository = Depends(get_repository(TrackerRepository))
    ) -> List[dict]:    
    return await ReportService.get_report_stay(day, property_repo, tracker_repo)

@router.get("/summary-movement/{speed}")
async def get_tracker_day(
        day:str,
        speed: int,
        tracker_repo: TrackerRepository = Depends(get_repository(TrackerRepository))
    ) -> List[dict]:
    
    return await ReportService.get_report_movement(day, speed, tracker_repo)