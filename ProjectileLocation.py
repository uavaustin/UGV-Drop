"""
The ProjectileLocation translates the the location of a projectile in Latitude and Longitude into a coordinate system.
This class should be run in tandem with the ProjectileDrop file.

@author: rishthak

"""

import math

"""
The point class specifies a point in three dimensions
    @param xComp The X Component running laterally to the ground
    @param xComp The Y Component perpendicular to the ground. The ground is presumed to be 0
    @param xComp The Z Component longitudinal to the ground

"""
class point:
    def __init__(self, xComp: float, yComp: float, zComp: float):
        self.x = xComp
        self.y = yComp
        self.z = zComp
    def __str__(self):
        return ("X: "  + str(self.x) + " Y: " + str(self.y) + " Z: " + str(self.z))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def setX(self, newX: float):
        self.x = newX

    def setY(self, newY: float):
        self.y = newY

    def setZ(self, newZ: float):
        self.z = newZ

"""
The vector class specifies a vector in three dimensions
    @param xComp The X Component running laterally to the ground
    @param yComp The Y Component longitudinal to the ground
    @param ZComp The Z Component perpendicular to the ground. The ground is presumed to be 0. I.E height

"""
class vector:
    def __init__(self, xComp: float, yComp: float, zComp: float):
        self.x = xComp
        self.y = yComp
        self.z = zComp

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

"""
The pointLatLon class specifies a vector in three dimensions
    @param Latitude The latitude
    @param Longitude The longitdue
    @param Altitude The altitude

"""
class pointLatLon:
    def __init__(self, Latitude: float, Longitude: float, Altitude: float):
        self.lat = Latitude
        self.lon = Longitude
        self.alt = Altitude

    def getLat(self):
        return self.lat

    def getLon(self):
        return self.lon

    def getAlt(self):
        return self.alt

"""
The alignToOriginTool can be used to translate a pointLatLon to a point at a specified origin
    @param observationPoint The pointLatLon defined as the observation location
    @param originPoint The pointLatLon defined as the origin

"""

class alignToOriginTool:
    def __init__(self, observationPoint: pointLatLon, originPoint: pointLatLon):
        self.obsPoint = observationPoint
        self.orgPoint = originPoint
        self.rEarth = 6378137 #equatorial raidus Earth

    def alignToOrigin(self, observationPoint: pointLatLon):
        self.obsPoint = observationPoint
        x = math.cos(self.obsPoint.getLat())*math.sin((self.obsPoint.getLon()-self.orgPoint.getLon())/2)
        x = math.asin(x)
        x = 2*self.rEarth*x
        y =self.rEarth*(self.obsPoint.getLat() - self.orgPoint.getLat())
        z = self.obsPoint.getAlt()
        cartesPoint = point(x,y,z)
        print("cartesian Point: " + str(cartesPoint))
        return cartesPoint

    def updateObsvPoint(self, observationPoint: pointLatLon):
        self.obsPoint = observationPoint

    def updateOrigin(self, originPoint: pointLatLon):
        self.orgPoint = pointOrigin
