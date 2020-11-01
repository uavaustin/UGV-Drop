import unittest
import math
from CartesianCoordinate import *

class geoCord:
    def __init__(self, Latitude: float, Longitude: float, Altitude: float):
        self.__lat = Latitude
        self.__lon = Longitude
        self.__alt = Altitude
    def __str__(self):
        return ("LAT: "  + str(self.__lat) + " LON: " + str(self.__lon) + " ALT: " + str(self.__alt))

    def getLat(self):
        return self.__lat

    def getLon(self):
        return self.__lon

    def getAlt(self):
        return self.__alt



"""
The alignToOriginTool can be used to translate a geoCord to a point at a specified origin
    @param observationPoint The geoCord defined as the observation location
    @param originPoint The geoCord defined as the origin

"""

class alignToOriginTool:
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
        print("cartesian Point: " + str(cartesPoint))
        return cartesPoint

    def updateObsvPoint(self, observationPoint: geoCord):
        self.__obsPoint = observationPoint

    def updateOrigin(self, originPoint: geoCord):
        self.__orgPoint = originPoint


"""
Unit testing section
"""

class TestMethods(unittest.TestCase):

#test alignToOriginTool class and its methods
    def testAlignToolMethods(self):
        observe = geoCord(-7.5, 10, 25)
        origin = geoCord(0, 0, 0)
        testOriginTool = alignToOriginTool(observe, origin)

        testAlignCase = testOriginTool.alignToOrigin(geoCord(2, -5, 8))
        self.assertAlmostEqual(testAlignCase.getX(), 3210774.4160264)
        self.assertAlmostEqual(testAlignCase.getY(), 12756274)
        self.assertAlmostEqual(testAlignCase.getZ(), 8)

        testOriginTool.updateObsvPoint(geoCord(-27, 12, 6))
        self.assertEqual(testOriginTool._alignToOriginTool__obsPoint.getLat(), -27)
        self.assertEqual(testOriginTool._alignToOriginTool__obsPoint.getLon(), 12)
        self.assertEqual(testOriginTool._alignToOriginTool__obsPoint.getAlt(), 6)

        testOriginTool.updateOrigin(geoCord(1, -1, 10))
        self.assertEqual(testOriginTool._alignToOriginTool__orgPoint.getLat(), 1)
        self.assertEqual(testOriginTool._alignToOriginTool__orgPoint.getLon(), -1)
        self.assertEqual(testOriginTool._alignToOriginTool__orgPoint.getAlt(), 10)


if __name__ == '__main__':
    unittest.main()
