from typing import List
from fastapi import APIRouter
from app.api.services.report import ReportService

router = APIRouter()

@router.get("/summary-stay/{day}")
async def get_tracker_day(day) -> List[dict]:    
    return ReportService.get_report_stay(day)

@router.get("/summary-movement/{speed}")
async def get_tracker_day(speed) -> List[dict]:
    report = [
        {"from": 1.5235, "to": 4.656225},
        {"from": 2.36522, "to": 6.3625554}
    ]
    return report    