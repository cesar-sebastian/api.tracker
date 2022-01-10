from app.db.repositories.base import BaseRepository
from app.models.tracker import Tracker

CREATE_TRACKER_QUERY = """
    INSERT INTO tracker (name, lat, lon, date)
    VALUES (:name, :lat, :lon, :date)
    RETURNING id, name, lat, lon, date;
"""

class TrackerRepository(BaseRepository):
    """
    All database actions associated with the property resource
    """

    async def create_tracker(self, *, new_tracker: Tracker) -> bool:
        query_values = new_tracker.dict()
        tracker = await self.db.fetch_one(query=CREATE_TRACKER_QUERY, values=query_values)
        return Tracker(**tracker)
