"""
Conversions
"""
import math
from CartesianCoordinate import *
from CartesianVector import *
from GeographicalCoordinate import *
"""
The alignToOriginTool can be used to translate a geoCord to a point at a specified origin
    @param observationPoint The geoCord defined as the observation location
    @param originPoint The geoCord defined as the origin

"""

class pointConversionTool:
    def __init__(self, observationPoint: geoCord, originPoint: geoCord):
        self.__obsPoint = observationPoint
        self.__orgPoint = originPoint
        self.__rEarth = 6378137 #equatorial raidus Earth

    def alignToOrigin(self, observationPoint: geoCord):
        self.__obsPoint = observationPoint
        x = math.cos(self.__obsPoint.getLat())*math.sin((self.__obsPoint.getLon()-self.__orgPoint.getLon())/2)
        x = math.asin(x)
        x = 2*self.__rEarth*x
        y =self.__rEarth*(self.__obsPoint.getLat() - self.__orgPoint.getLat())
        z = self.__obsPoint.getAlt()
        cartesPoint = point(x,y,z)
        #print("cartesian Point: " + str(cartesPoint))
        return cartesPoint

    def updateObsvPoint(self, observationPoint: geoCord):
        self.__obsPoint = observationPoint

    def updateOrigin(self, originPoint: geoCord):
        self.__orgPoint = pointOrigin

    def pointToGeoCord(self, transPoint: point):
        x = transPoint.getX()
        y = transPoint.getY()
        alt = transPoint.getZ()
        lon = (y/self.__rEarth) + self.__orgPoint.getLon()
        lat = x/(2*self.__rEarth)
        lat = lat/(math.sin((lon - self.__orgPoint.getLon())/2))
        lat = math.acos(math.sin(lat))
<<<<<<< HEAD
        return geoCord(lat, lon, alt)
=======
        return geoCord(lat, lon, alt)
>>>>>>> defc6fe1958213fb22bc7c8eef0e8b31054164a3
