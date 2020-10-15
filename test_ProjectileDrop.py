"""

unit testing for ProjecileDrop.py
Assumptions:
    Max Y = 30.48
    No negative components for points class
    ?Target is origin?

@author: jordan

"""
import unittest
from ProjectileDrop import *

class TestMethods(unittest.TestCase):

#test point class and methods
    def testPointMethods(self):
        x = 10
        y = 6.5
        z = 21.4
        testPoint = point(x, y, z)

        self.assertEqual(testPoint.getX(), x)
        self.assertEqual(testPoint.getY(), y)
        self.assertEqual(testPoint.getZ(), z)

        testPoint.setX(13)
        testPoint.setY(2.0)
        testPoint.setZ(29.8888)

        self.assertEqual(testPoint.getX(), 13)
        self.assertEqual(testPoint.getY(), 2)
        self.assertEqual(testPoint.getZ(), 29.8888)

#test vector class and methods
    def testVectorMethods(self):
        xv = 14.76
        yv = -5.4321
        zv = -9.426
        testVector = vector(xv, yv, zv)

        self.assertEqual(testVector.getX(), xv)
        self.assertEqual(testVector.getY(), yv)
        self.assertEqual(testVector.getZ(), zv)

#testing all dropCalculations methods
    def testDropCalcMethods(self):
        velVec = vector(10, 2, -3)
        accelVec = vector(-1, 20, 3)
        projLoc = point(12, 5.5, 0.6)
        targetLoc = point(0, 0, 0)
        coeffDrag = 0.1
        chuteAndUGVMass = 20
        chuteArea = 70
        chuteDeployTime = 2

        testDropCalc = dropCalculations(velVec,accelVec,projLoc,targetLoc,coeffDrag,chuteAndUGVMass,chuteArea,chuteDeployTime)

        testDropCalc.updateLocation(1,2,3):
        self.assertEqual(testDropCalc.projX, 1)
        self.assertEqual(testDropCalc.projY, 2)
        self.assertEqual(testDropCalc.projZ, 3)
#this is not done lol



if __name__ == '__main__':
    unittest.main()
