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
        return geoCord(lat, lon, alt)


class TestMethods(unittest.TestCase):

    def testPointToGeo(self):
        observe = geoCord(-0.001, -0.002, 2)
        origin = geoCord(0, 0, 0)
        testConversion = pointConversionTool(observe, origin)

        testResult = testConversion.pointToGeoCord(point(-.01, 1, .01))
        self.assertAlmostEqual(testResult.getLat(),1.58079632679)
        self.assertAlmostEqual(testResult.getLon(),.00000015678559429)
        self.assertAlmostEqual(testResult.getAlt(),.01)

    def testAlignToOrigin(self):
        observe = geoCord(-7.5, 10, 25)
        origin = geoCord(0, 0, 0)
        testConversion = pointConversionTool(observe, origin)
        testAlignCase = testConversion.alignToOrigin(geoCord(2, -5, 8))

        self.assertAlmostEqual(testAlignCase.getX(), 3210774.4160264)
        self.assertAlmostEqual(testAlignCase.getY(), 12756274)
        self.assertAlmostEqual(testAlignCase.getZ(), 8)

    """
    def testUpdateMethods(self):
        observe = geoCord(-0.001, -0.002, 2)
        origin = geoCord(0, 0, 0)
        testConversion = pointConversionTool(observe, origin)
        testConversion.updateObsvPoint(geoCord(-.05681216597, 12.456879, 6))
        self.assertEqual(testConversion.__obsPoint.getLat(), -.05681216597)
        self.assertEqual(testConversion.__obsPoint.getLon(), 12.456879)
        self.assertEqual(testConversion.__obsPoint.getAlt(), 6)
        testConversion.updateOrigin(geoCord(1, -1, 9001))
        self.assertEqual(testConversion.__orgPoint.getLat(), 1)
        self.assertEqual(testConversion.__orgPoint.getLon(), -1)
        self.assertEqual(testConversion.__orgPoint.getAlt(), 9001) #its over 9000!
        #these don't work yet
    """


if __name__ == '__main__':
    unittest.main()
