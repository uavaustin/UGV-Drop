"""
Conversions
"""
import math
import unittest
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
        self.__obsPoint = geoCord(self.__obsPoint.getLat() * (math.pi / 180),
                                     self.__obsPoint.getLon() * (math.pi / 180),
                                     self.__obsPoint.getAlt())
        self.__orgPoint = geoCord(self.__orgPoint.getLat() * (math.pi / 180),
                                     self.__orgPoint.getLon() * (math.pi / 180),
                                     self.__orgPoint.getAlt())
        self.__rEarth = 6378137  # equatorial radius Earth

    def degToRadians(self, obsPoint: geoCord  ):
        #Convert to Radians
        radPoint = geoCord(obsPoint.getLat()*(math.pi/180),
                           obsPoint.getLon()*(math.pi / 180),
                           obsPoint.getAlt())
        return radPoint

    def alignToOrigin(self, observationPoint: geoCord):
        self.__obsPoint = self.degToRadians(observationPoint)
        x = math.cos(self.__obsPoint.getLat())*math.sin((self.__obsPoint.getLon()-self.__orgPoint.getLon())/2)
        x = math.asin(x)
        x = 2*self.__rEarth*x *(180/math.pi)
        y =self.__rEarth*(self.__obsPoint.getLat() - self.__orgPoint.getLat()) *(180/math.pi)
        z = self.__obsPoint.getAlt()
        cartesPoint = point(x,y,z)
        print("cartesian Point: " + str(cartesPoint))
        return cartesPoint

    def pointToOrgS(self, pointObs: point, ):


    def updateObsvPoint(self, observationPoint: geoCord):
        self.__obsPoint = observationPoint

    def updateOrigin(self, originPoint: geoCord):
        self.__orgPoint = originPoint

    def pointToGeoCord(self, transPoint: point):
        print("TransPoint" + str(transPoint))
        x = transPoint.getX()*math.pi/180
        y = transPoint.getY()*math.pi/180
        alt = transPoint.getZ()
        lon = (y/self.__rEarth) + self.__orgPoint.getLon()*(180/math.pi)
        lat = x/(2*self.__rEarth)
        lat = lat/(math.sin((lon - self.__orgPoint.getLon())/2))
        lat = math.acos(math.sin(lat)) *(180/math.pi)
        print("ObsPoint" + str(self.__obsPoint))
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



if __name__ == '__main__':
    unittest.main()
    
