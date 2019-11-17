from geopy.geocoders import Nominatim

class Car:
    pass
    def __init__(self, geolocator):

        def gps(self, location):
            self.geolocator = Nominatim()
            location = self.geolocator.geocode("175 5th Avenue NYC")
            print(location.address)
            print((location.latitude, location.longitude))
            return location