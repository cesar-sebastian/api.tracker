from datetime import date
from app.models.core import CoreModel

class Report(CoreModel):
    property: str
    time: int
    day: date