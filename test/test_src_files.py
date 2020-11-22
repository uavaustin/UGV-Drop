"""
Unit testing for all files in src except __init__.py

"""

import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from src import *
import unittest


class TestMethods(unittest.TestCase):

    #CartesianCoordinate
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


    #CartesianVector
    def testVectorMethods(self):
        xv = 14.76
        yv = -5.4321
        zv = -9.426
        testVector = vector(xv, yv, zv)

        self.assertEqual(testVector.getX(), xv)
        self.assertEqual(testVector.getY(), yv)
        self.assertEqual(testVector.getZ(), zv)


    #CartGeoConversions
    def testAlignToOrgin(self):
        observe = geoCord(-7.5, 10, 25)
        origin = geoCord(0, 0, 0)
        testConversion = pointConversionTool(observe, origin)
        testAlignCase = testConversion.alignToOrigin(geoCord(2, -5, 8))

        self.assertAlmostEqual(testAlignCase.getX(), 3210774.4160264)
        self.assertAlmostEqual(testAlignCase.getY(), 12756274)
        self.assertAlmostEqual(testAlignCase.getZ(), 8)


    #GeographicalCoordinate
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


    #UGVDropCalculator
    #...
    #haven't been written yet

if __name__ == '__main__':
    unittest.main()
