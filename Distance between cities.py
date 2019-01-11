from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="Distance between cities")

def get_location_one(place):
    location = geolocator.geocode(place)

    return location


place_one = input("Please enter first City: ")
location_one = get_location_one(place_one)

place_two = input("Please enter second City: ")
location_two = get_location_one(place_two)

place_one_cor = (location_one.latitude, location_one.longitude)
place_two_cor = (location_two.latitude, location_two.longitude)

distance = geodesic(place_one_cor, place_two_cor).kilometers
print(f"Distance between {place_one} and {place_two} is {round(distance)} kilometers")



