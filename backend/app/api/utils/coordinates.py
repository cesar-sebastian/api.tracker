from haversine import haversine, Unit

'''
200 m radio
'''
RADIO = 0.2 

def isProperty(geo_property: tuple, geo_tracker: tuple) -> bool:
    return RADIO <= haversine(geo_property, geo_tracker)