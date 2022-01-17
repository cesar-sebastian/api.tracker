from typing import List
from app.db.repositories.tracker import TrackerRepository
from app.db.repositories.property import PropertyRepository
from app.models.report import Report
from app.api.utils import coordinates
from datetime import datetime, timedelta

class ReportService():

    async def get_report_stay(
            day: str,
            property_repo: PropertyRepository,
            tracker_repo: TrackerRepository
        ) -> List[Report]:

        date_from = datetime.strptime(day, '%Y-%m-%d')
        date_to = date_from + timedelta(days=1)
        properties = await property_repo.fetch_all()        
        trackers = await tracker_repo.fetch_trackers(date_from, date_to)
        
        property_traker = {}
        
        for property in properties:            
            trackers_time = []
            for tracker in trackers:
                isInclude = coordinates.isProperty((property.lat, property.lon), (tracker.lat, tracker.lon))
                print((property.lat, property.lon), (tracker.lat, tracker.lon))
                print(isInclude)
                if isInclude == True:
                    trackers_time.append(tracker.created_at)
                    #trackers.pop(tracker)
            
            if len(trackers_time) > 0:
                property_traker[property.name] = trackers_time

        report = []
        for name in property_traker:
            time = (property_traker[name][-1] - property_traker[name][0]) / timedelta(milliseconds=1)  
            report.append(Report(property=name, time=time, day=day))
        
        return report

    async def get_report_movement(
            day: str,
            speed: int,
            tracker_repo: TrackerRepository
        ) -> List:
        
        date_from = datetime.strptime(day, '%Y-%m-%d')
        date_to = date_from + timedelta(days=1)
        trackers = await tracker_repo.fetch_trackers(date_from, date_to)
        result = []
        tracker_0 = None
        for tracker in trackers: 
            if tracker_0 is not None:
                distance = coordinates.distance((tracker.lat, tracker.lon),(tracker_0.lat, tracker_0.lon))
                time_diff = (tracker.created_at - tracker_0.created_at) / timedelta(seconds=1)
                v = distance / time_diff
                if speed <= v:
                    result.append({
                        'from': {
                            'lat': tracker_0.lat,
                            'lon': tracker_0.lon
                        },
                        'to': {
                            'lat': tracker_0.lat,
                            'lon': tracker_0.lon
                        }
                    })
        
        return result




