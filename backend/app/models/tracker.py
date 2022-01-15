from app.models.core import IDModelMixin, DateTimeModelMixin

class Tracker(IDModelMixin, DateTimeModelMixin):
    lat: float
    lon: float