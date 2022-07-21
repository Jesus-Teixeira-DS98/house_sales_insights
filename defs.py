
import time
from geopy.geocoders import Nominatim

geolocator = Nominatim( user_agent='geopiExercises' )

def get_longlat( x ):
    index, row = x
    time.sleep(1)
    response = geolocator.reverse( row['query'] )
    address = response.raw['address']

    try:
        road = address['road'] if 'road' in address else 'NA'
        house_number = address['house_number'] if 'house_number' in address else 'NA'
        neighbourhood = address['neighbourhood'] if 'neighbourhood' in address else 'NA'


        return road, house_number, neighbourhood

    except:
        return None, None, None