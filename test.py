from haversine import haversine_vector, Unit
from math import radians, cos, sin, asin, sqrt

def haversineAlt(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

#megatlon -34.648806501319825, -58.37642899221854
#mi casa  -34.644326064957106, -58.39287193144872
#center_point = [{'lat': -7.7940023, 'lng': 110.3656535}]
#test_point = [{'lat': -7.79457, 'lng': 110.36563}]

megatlon = (-34.648806501319825, -58.37642899221854)
micasa = (-34.644326064957106, -58.39287193144872)
miexcasa = (-34.6179672866717, -58.44856120679429)

property = (-34.648872228362585, -58.376403759816014)
tracker = (-34.63991592366364, -58.37771672692084)
 

print(haversine_vector([property], [tracker], unit=Unit.KILOMETERS))

'''
center_point = [{'lat': -34.648806501319825, 'lng': -58.37642899221854}]
test_point = [{'lat': -34.644326064957106, 'lng': -58.39287193144872}]

lat1 = center_point[0]['lat']
lon1 = center_point[0]['lng']
lat2 = test_point[0]['lat']
lon2 = test_point[0]['lng']

radius = 0.5 # in kilometer

a = haversineAlt(lon1, lat1, lon2, lat2)

print('Distance (km) : ', a)
if a <= radius:
    print('Inside the area')
else:
    print('Outside the area')
'''