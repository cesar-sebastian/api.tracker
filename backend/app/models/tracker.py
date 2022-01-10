
from app.models.core import CoreModel
from datetime import datetime

class Tracker(CoreModel):
    lat: float
    lon: float
    date: datetime