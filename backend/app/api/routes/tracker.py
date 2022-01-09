from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.post("/tracker")
def create_tracker() -> List[dict]:
    report = [
        {"id": 1, "name": "My house", "cleaning_type": "full_clean", "price_per_hour": 29.99},
        {"id": 2, "name": "Someone else's house", "cleaning_type": "spot_clean", "price_per_hour": 19.99}
    ]
    return report
