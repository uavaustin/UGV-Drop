"""
The CartGeoConversions converts cartesian information into a geographical coordinate based on a specified origin.

@author: rishthak, jordan

"""
import math
import unittest
from CartesianCoordinate import *
from CartesianVector import *
from GeographicalCoordinate import *

"""
The alignToOriginTool can be used to translate a geoCord to a point at a specified origin. This method is observation
location independent. In other words, you just need to know how far the projectile will drop, not where it is.
    @param observationPoint The geoCord defined as the final position of the projectile if it were to drop based on the
        calculated drop displacement vector and land at (0, 0, 0,).
        NOTE: This DOES NOT treat the projectile as the origin. The drop location is still the origin.
    @param originPoint The geoCord defined as the origin

"""

class cartGeoConv:

    def alignToOrgin(pointObs: point, dropGeoCord: geoCord):
        # Naming convention (dimension)(location/origin)(R: radians, D: Degrees)
        #Cartesian of where to drop from
        x = 0-pointObs.getX()
        y = 0-pointObs.getY()
        alt = pointObs.getZ()
        R = 6378137 #equatorial raidus at earth

        #Geographical of where to go expressed in radians
        latOR = math.radians(dropGeoCord.getLat())
        lonOR = math.radians(dropGeoCord.getLon())

        #Finding where to Drop From in radians
        latLR = ((y/R) + latOR)
        lonLR = x/(2*R*math.asin(math.cos(latOR)))
        lonLR = math.asin(lonLR) + (lonOR/2)
        lonLR = lonLR*2

        #Converting back from radians to degrees
        latLD = math.degrees(latLR)
        lonLD = math.degrees(lonLR)
        output = geoCord(latLD, lonLD, alt)
        return output




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
