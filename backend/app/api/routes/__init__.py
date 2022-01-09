from fastapi import APIRouter
from app.api.routes.report import router as report_router
from app.api.routes.tracker import router as tracker_router

router = APIRouter()

router.include_router(report_router, prefix="/report", tags=["report"])
router.include_router(tracker_router, prefix="/tracker", tags=["tracker"])
