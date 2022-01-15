from optparse import Values
from app.db.repositories.base import BaseRepository
from app.models.tracker import Tracker
from typing import List

CREATE_TRACKER_QUERY = """
    INSERT INTO tracker (lat, lon)
    VALUES (:lat, :lon)
    RETURNING id, lat, lon;
"""

SELECT_TRACKER_BY_DAY = """
    SELECT * 
    FROM tracker
    WHERE created_at >= :date_from
    AND created_at < :date_to
    ORDER BY created_at ASC;
"""

class TrackerRepository(BaseRepository):
    """
    All database actions associated with the property resource
    """

    async def create_tracker(self, *, new_tracker: Tracker) -> Tracker:
        query_values = new_tracker.dict()
        tracker = await self.db.fetch_one(query=CREATE_TRACKER_QUERY, values=query_values)
        return Tracker(**tracker)

    async def fetch_trackers(self, date_from, date_to) -> List[Tracker]:
        trackers = await self.db.fetch_all(
            query=SELECT_TRACKER_BY_DAY,
            values={"date_from": date_from, 'date_to': date_to}
        )

        return [Tracker(**l) for l in trackers]