"""
Unit tests for ProjectileLocation

@author: Jordan

assumptions:
    points and vectors can have negative components
    max height is like 30 meters(i think)

"""

import unittest
from ProjectileLocation import *

class TestMethods(unittest.TestCase):

#test point class and its methods
    def testPointMethods(self):
        x = 10
        y = -6.5
        z = 21.4
        testPoint = point(x, y, z)

        self.assertEqual(testPoint.getX(), x)
        self.assertEqual(testPoint.getY(), y)
        self.assertEqual(testPoint.getZ(), z)

        testPoint.setX(-13)
        testPoint.setY(-2.0)
        testPoint.setZ(29.8888)

        self.assertEqual(testPoint.getX(), -13)
        self.assertEqual(testPoint.getY(), -2)
        self.assertEqual(testPoint.getZ(), 29.8888)

#test vector class and its methods
    def testVectorMethods(self):
        xv = 14.76
        yv = -5.4321
        zv = -9.426
        testVector = vector(xv, yv, zv)

        self.assertEqual(testVector.getX(), xv)
        self.assertEqual(testVector.getY(), yv)
        self.assertEqual(testVector.getZ(), zv)

#test pointLatLon class and its methods
    def testpointLatLon(self):
        lat = 25.88485
        lon = -13.48790
        alt = 10.1546
        testLatLon = pointLatLon(lat, lon, alt)

        self.assertEqual(testLatLon.getLat(), 25.88485)
        self.assertEqual(testLatLon.getLon(), -13.48790)
        self.assertEqual(testLatLon.getAlt(), 10.1546)

#test alignToOriginTool class and its methods
    def testOriginToolMethods(self):
        observe = pointLatLon(-7.5, 10, 25)
        origin = pointLatLon(0, 0, 0)
        testOriginTool = alignToOriginTool(observe, origin)
        """
        self.assertAlmostEqual(testOriginTool.alignToOrigin(pointLatLon(2, -5, 8)), #the calculated value)
        #not calculated yet
        """
        testOriginTool.updateObsvPoint(pointLatLon(-27, 12, 6))

        testOriginTool.updateOrigin(pointLatLon(1, -1, 10))
        self.assertEqual(testOriginTool.orgPoint.getLat(), 1)
        self.assertEqual(testOriginTool.orgPoint.getLon(), -1)
        self.assertEqual(testOriginTool.orgPoint.getAlt(), 10)





if __name__ == '__main__':
    unittest.main()
