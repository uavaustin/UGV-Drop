"""
unit testing UGV drop projectile

author : sydney rabara

assume:
maxY = 30.48
No negative components for points class
The target is origin



"""

import unittest

from ProjectileDrop import *

class TestMethods(inittest,TestCase):

#test the points
    def testPointMethods(self):
        x = 60.2221;
        y = 80.0778;
        z = 54.28;
        testPoint = point(x,y,z);

        self.assertEqual(testPoint.getX(),x)
        self.assertEqual(testPoint.getY(),Y)
        self.assertEqual(testPoint.getZ(),Z)

        testPoint.setX(100.774)
        testPoint.setY(59.0012)
        testPoint.setZ(78.342)

        self.assertEqual(testPoint.getX(),100.774)
        self.assertEqual(testPoint.getX(),59.0012)
        self.assertEqual(testPoint.getX(),78.342)

#test vector
  def testVectorMethods(self):
        xv = 14.76
        yv = -5.4321
        zv = -9.426
        testVector = vector(xv, yv, zv)

        self.assertEqual(testVector.getX(), xv)
        self.assertEqual(testVector.getY(), yv)
        self.assertEqual(testVector.getZ(), zv)

#test drop calc

    def testDropCalcMethods(self):
        velVec = vector(9, 2, 0)
        accelVec = vector(2,8,10)
        projLoc = point(34.77,39.1110,65.78)
        targetLoc = point(0,0,0) #origin
        coeffD = 0.1 #coefficient of drag
        chute_UGV_mass = 20 #kg?
        chute_A = 60 #area in m^2?
        chute_deploy_t = 5 #chute deploy testPointMethods

        testDropCalc = dropCalculations(velVec,accelVec,projLoc,targetLoc,coeffD, chute_UGV_mass, chute_A, chute_deploy_t)

        testDropCalc.updateLocation(1,2,3):
        self.assertEqual(testDropCalc.projX,1)
        self.assertEqual(testDropCalc.projY,2)
        self.assertEqual(testDropCalc.projZ,3)

        testDropCalc.updateVelocity(1,2,3):
        self.assertEqual(testDropCalc.projvX,1)
        self.assertEqual(testDropCalc.projvX,2)
        self.assertEqual(testDropCalc.projvX,3)
