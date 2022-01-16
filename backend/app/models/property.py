from app.models.core import CoreModel
from app.models.core import IDModelMixin, DateTimeModelMixin

class PropertyBase(CoreModel):
    name: str
    lat: float
    lon: float

class PropertyCreate(PropertyBase):
    pass

class PropertyInDB(IDModelMixin):
    name: str
    lat: float
    lon: float

class PropertyPublic(PropertyBase):
    pass