from app.models.core import CoreModel

class Property(CoreModel):
    name: str
    lat: float
    lon: float