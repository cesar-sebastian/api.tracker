from app.db.repositories.base import BaseRepository
from typing import List
from app.models.property import Property

SELECT_PROPERTY = """
    SELECT name, lat, lon
    FROM property;
"""

class PropertyRepository(BaseRepository):
    """
    All database actions associated with the property resource
    """

    async def fetch_all(self) -> List[Property]:
        properties = await self.db.fetch_all(
            query=SELECT_PROPERTY
        )
        
        return [Property(**l) for l in properties]

