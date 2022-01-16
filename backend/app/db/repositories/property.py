from app.db.repositories.base import BaseRepository
from typing import List
from app.models.property import PropertyInDB, PropertyCreate

CREATE_PROPERTY_QUERY = """
    INSERT INTO property (name, lat, lon)
    VALUES (:name, :lat, :lon)
    RETURNING id, name, lat, lon;
"""

SELECT_PROPERTY = """
    SELECT name, lat, lon
    FROM property;
"""

class PropertyRepository(BaseRepository):
    """
    All database actions associated with the property resource
    """

    async def create_property(self, *, new_property: PropertyCreate) -> PropertyInDB:
        query_values = new_property.dict()
        property = await self.db.fetch_one(query=CREATE_PROPERTY_QUERY, values=query_values)
        return PropertyInDB(**property)

    async def fetch_all(self) -> List[PropertyInDB]:
        properties = await self.db.fetch_all(
            query=SELECT_PROPERTY
        )        
        return [PropertyInDB(**l) for l in properties]

