from app.models.core import IDModelMixin, DateTimeModelMixin
from app.models.core import CoreModel

class TrackerBase(CoreModel):
    lat: float
    lon: float

class TrackerCreate(TrackerBase):    
    pass

class TrackerInDB(IDModelMixin, DateTimeModelMixin):
    lat: float
    lon: float

class TrackerPublic(TrackerBase, DateTimeModelMixin):
    pass

