import math

class Coordinates(object):
    EARTH_RADIUS = 6371000.0


    def __init__(self, latitude, longitude):
        self.latitude = math.radians(latitude)
        self.longitude = math.radians(longitude)
        # replace pass with your code
        #pass


    def distance_to(self, other):
        p1 = 2*6371000.0
        lats = (self.latitude - other.latitude)/2
        longs = (self.longitude - other.longitude)/2
        sin_lat = math.pow(lats, 2)
        sin_longs = math.pow(longs, 2)
        x = math.sqrt(sin_lat + math.cos(other.latitude)*math.cos(self.latitude)*
            sin_longs)
        asin = math.asin(x)

        dist = p1*asin

        # your code here
        # replace 0.0 with appropriate return value
        return dist


    def __repr__(self):       
        return "({}, {})".format(self.latitude, self.longitude)
        # your code here
        # replace "" with appropriate return value
        




    #def convert_to_rads(latitude, longitude):
        #rad_lat = math.radians(latitude)
        #rad_long = math.radians(longitude)
        #return rad_lat, rad_long
        #rad_lat = math.radians(latitude)
        #rad_long = math.radians(longitude)
        #print(rad_lat)
        #print(rad_long)
        #return rad_lat, rad_long
