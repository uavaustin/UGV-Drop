"""
The ProjectileLocation translates the the location of a projectile in Latitude and Longitude into a coordinate system.
This class should be run in tandem with the ProjectileDrop file.

"""

class pointLatLon:
    def __init__(self, Latitude: float, Longitude: float):
        self.lat = Latitude
        self.long = Longitude

    def getLat(self)
        return self.lat

    def getLon(self)
        return self.lon

class alignToOrigin:
    def __init__(self, originLatitude: float, originLongitude: float):
        self.orLat = originLatitude
        self.orLon = originLongitude
        self.orX = 0
        self.orY = 0

    def translatePoint(self, sourceLatitude: float, sourceLongitude: float):
        latLonVectorMag = sourceLatitude**2 + sourceLongitude**2
        latLonVectorMag = math.sqrt(latLonVectorMag)
