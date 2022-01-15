from contextlib import nullcontext
from typing import List
from app.db.repositories.tracker import TrackerRepository
from app.db.repositories.property import PropertyRepository
from app.api.dependencies.database import get_repository
from app.models.report import Report
from fastapi import Depends
from app.api.utils import coordinates
import datetime

class ReportService():

    def get_report_stay(day) -> List[Report]:

        date_from = datetime.datetime.strptime(day, "%m/%d/%y")
        date_to = date_from + datetime.timedelta(days=1)

        tracker_repo: TrackerRepository = Depends(get_repository(TrackerRepository))
        property_repo: PropertyRepository = Depends(get_repository(PropertyRepository))
        properties = property_repo.fetch_all()
        trackers = tracker_repo.fetch_trackers_by_day(date_from.strftime('%Y-%m-%d'), date_to.strftime('%Y-%m-%d'))
        property_traker = {}
        
        for property in properties:            
            trackers_time = []
            for tracker in trackers:          
                if coordinates.isProperty((property.lat, property.lon), (tracker.lat, tracker.lon)):
                    trackers_time.append(property.date)
                    trackers.pop(tracker)
            
            if tracker_repo.len() > 0:
                property_traker[property.name] = trackers_time

        report = []
        for name in property_traker:
            time = property_traker[name][-1] - property_traker[name][0]
            report.append(Report(name, time, day))
        
        return report



