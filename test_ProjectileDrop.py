"""

unit testing for ProjecileDrop.py
Assumptions:
    Z is height: Max Z = 30.48
    Target is origin, so negative points are allowed

@author: jordan

"""
import unittest
from ProjectileDrop import *

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

#testing all dropCalculations methods
    def testDropCalcMethods(self):
        velVec = vector(10, 2, -3)
        accelVec = vector(-1, 20, 3)
        projLoc = point(12, 5.5, 0.6)
        targetLoc = point(0, 0, 0)
        coeffDrag = 0.1
        ProjSysMass = 20
        chuteArea = 70
        chuteDeployTime = 2
        #setting up values to use in the methods
        testDropCalc = dropCalculations(velVec,accelVec,projLoc,targetLoc,coeffDrag,ProjSysMass,chuteArea,chuteDeployTime)

        #test updateLocation

        testDropCalc.updateLocation(1,2,3)
        self.assertEqual(testDropCalc.projX, 1)
        self.assertEqual(testDropCalc.projY, 2)
        self.assertEqual(testDropCalc.projZ, 3)

        #test updateVelocity
        testDropCalc.updateVelocity(2,-2,0)
        self.assertEqual(testDropCalc.vX, 2)
        self.assertEqual(testDropCalc.vY, -2)
        self.assertEqual(testDropCalc.vZ, 0)

        #test updateAcceleration
        testDropCalc.updateAcceleration(-9,8,-7)
        self.assertEqual(testDropCalc.aX,-9)
        self.assertEqual(testDropCalc.aY,8)
        self.assertEqual(testDropCalc.aZ,-7)

        #test updateAirDensity
        testDropCalc.updateAirDensity(.54)
        self.assertEqual(testDropCalc.airDensity, .54)

        #test updateChuteDepTime
        testDropCalc.updateChuteDepTime(3.6)
        self.assertEqual(testDropCalc.chuteDepTime, 3.6)

        #test calcDescentVelocity
        testDropCalc.calcDescentVelocity()
        self.assertAlmostEqual(testDropCalc.vYpost, -10.1886958837)

        #test trueTimeToReachGround
        self.assertAlmostEqual(testDropCalc.trueTimeToReachGround(), 1.661527657)

        #test calcDropSpot
        dropSpot = testDropCalc.calcDropSpot()
        self.assertAlmostEqual(dropSpot.getX(), 114.05347447)
        self.assertAlmostEqual(dropSpot.getY(), 2)
        self.assertAlmostEqual(dropSpot.getZ(), 96.89285650)



if __name__ == '__main__':
    unittest.main()
