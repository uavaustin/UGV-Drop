"""
The ProjectileLocation translates the the location of a projectile in Latitude and Longitude into a coordinate system.
This class should be run in tandem with the ProjectileDrop file.

@author: rishthak

"""
"""
The point class specifices a point in three dimensions
"""


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
    @param xComp The Y Component perpendicular to the ground. The ground is presumed to be 0
    @param xComp The Z Component longitudinal to the ground

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

class pointLatLon:
    def __init__(self, Latitude: float, Longitude: float):
        self.lat = Latitude
        self.long = Longitude

    def getLat(self):
        return self.lat

    def getLon(self):
        return self.lon

class alignToOriginTool:
    def __init__(self, observationPoint: pointLatLon, originPoint: pointLatLon):
        self.obsPoint = observationPoint
        self.orgPoint = pointOrigin

    def alignToOrigin(self):
        return

    def updateObsvPoint(self, observationPoint: pointLatLon):
        self.obsPoint = observationPoint

    def updateOrigin(self, originPoint: pointLatLon):
        self.orgPoint = pointOrigin
