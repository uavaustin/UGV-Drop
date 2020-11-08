"""
The UGVDropCalculator calculates the location at which a projectile needs to be dropped to reach an intended target.

Inputs:
    * Drag Coefficient of the Parachute
    * Air Density
    * The Position Vector of the UGV
    * The Velocity Vector of the UGV
    * The Acceleration Vector of the UGV

Assumptions:
    The coefficient of drag for parachute is known.
    The Projectile vertically when during the time the chute is being deployed.

@author: rishthak

"""
import math
import time
import numpy
from CartesianGeographicalConversions import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import unittest





"""
The dropCalclations class specifices the location and time? when a projectile should dropped to land on a target
    Input variables can be updated if not immediately known.
    Only one instance of this class is required to compute the drop location for a continous calculation of the drop spot.
    All units are in metric units: meters, kg, seconds, etc.

    Input Variables:
     @param velocityVector      The initial velocity of the projectile
     @param obsPoint            The location of the projectile
     @param targetPoint         The location of the target
     @param coeffOfDragPhase1   The coefficient of drag during phase 1
     @param coeffOfDragPhase2   The coefficient of drag during phase 2
     @param dropProjSysMass     The mass of the system
     @param systemArea1         The area of the projectile in phase 1
     @param systemArea2         The area of the projectile in phase 2
     @param airDensity          The density of the air
     @param step                The time step for the solver
     @param deploymentHeight    The height at which phase 2 is intiated


TO USE THIS CLASS:
1. Create an instance with the properties of the projectile.
2. Update the position, velocity, and acceleration vectors every iteration.
3. Calculate the drop location using the calcDropSpot method every iteration.

"""
class dropCalculations:
    def __init__(self,
                velocityVector: vector,
                obsPoint: geoCord,
                targetPoint: geoCord,
                coeffOfDragPhase1: float,
                coeffOfDragPhase2: float,
                dropProjSysMass: float, #mass of parachute and UGV system
                systemArea1: float,
                systemArea2: float,
                airDensity: float,
                step: float,
                deploymentHeight: float):

        #Initializing the translator
        self.__translator = pointConversionTool(obsPoint, targetPoint)

        #NO LONGER NEEDED (Or Accurate)
        projectileLoc = self.__translator.alignToOrigin(obsPoint)
        targetLoc = point(0, 0, 0)

        #Phase 1 Phase 2 Drag Coefficients
        self.__dragCoeff1 = coeffOfDragPhase1
        self.__dragCoeff2 = coeffOfDragPhase2

        #Fixed Constants
        self.__mass = dropProjSysMass
        self.__g = -9.81 #acceleration due to gravity
        self.__airDensity = airDensity #in kg/m^3
        self.__sysA1 = systemArea1
        self.__sysA2 = systemArea2

        # UGV/Projectile Location NO LONGER NEEDED
        self.__projX = projectileLoc.getX()
        self.__projY = projectileLoc.getY()
        self.__projZ = projectileLoc.getZ()

        # Target Location
        self.__tarX = targetLoc.getX()
        self.__tarY = targetLoc.getY()
        self.__tarZ = targetLoc.getZ()

        #Only Used Target Location
        self.__targetGeo = targetPoint

        #velocities
        self.__vX = velocityVector.getX()
        self.__vY = velocityVector.getY()
        self.__vZ = velocityVector.getZ()

        #Iterator
        self.__step = step

        #Deployment Height
        self.__depHeight = deploymentHeight

        #Loading Data Arrays
        self.__xArr = []
        self.__yArr = []
        self.__zArr = []
        self.__zVelArr = []
        self.__zAccArr = []
        self.__tArr = []
        self.__dataSet = []
        self.__checkLoad = False

        #DebuggingToggle
        self.__debugPrintToggle = False

    def updateLocation(self, x: float, y: float, z: float):
        self.__projX = x
        self.__projY = y
        self.__projZ = z

    def updateVelocity(self, x: float, y: float, z: float):
        self.__vX = x
        self.__vY = y
        self.__vZ = z

    def updateAirDensity(self, newDensity: float):
        self.__airDensity = newDensity

    def updateChuteDepAltitude(self, newDepAlt: float):
        self.__depHeight = newDepAlt


    def calcDropSpot(self):
        theDispVector = self.dropIterator(self.__step, self.__depHeight, self.__sysA1, self.__sysA2)
        dropXComp = 0 - theDispVector.getX()
        dropYComp = 0 - theDispVector.getY()
        dropZComp = 0 - theDispVector.getZ()
        currentDropSpot = point(dropXComp, dropYComp, dropZComp)

        #Debugging Print Statements
        if self.__debugPrintToggle:
            print(theDispVector)
            print(currentDropSpot)

        self.__checkLoad = True
        return currentDropSpot

    def calcDropSpotGeoCord(self):
        coordinate = self.calcDropSpot()
        output = self.__translator.pointToOrgS(coordinate, self.__targetGeo)
        return output

    def forcesCalculator(self, dragCoeff: float, surfaceArea: float, vThisStep: vector):
        aX = (-1*numpy.sign(self.__vX))*((.5)*self.__airDensity*dragCoeff*surfaceArea*(vThisStep.getX()**2))/self.__mass
        aY= (-1*numpy.sign(self.__vY))*((.5)*self.__airDensity*dragCoeff*surfaceArea*(vThisStep.getY()**2))/self.__mass
        aZ = self.__g + ((.5)*self.__airDensity*dragCoeff*surfaceArea*(vThisStep.getZ()**2))/self.__mass

        #Debugging Print
        if self.__debugPrintToggle:
            print("step")
            print(str(vector(aX, aY, aZ)))
        #time.sleep(1)
        return vector(aX, aY, aZ)

    def dropIterator(self, timeInterval: float, deploymentHeight: float, a1: float, a2: float):

        step = timeInterval
        sCurr = point(0,0,0)
        vCurr = vector(self.__vX, self.__vY, self.__vZ)
        aNext = vector(0,0,0)
        tTotal = 0


        while(abs(self.__projZ + sCurr.getZ()) >  deploymentHeight):

            print("Current Altitude: " + str(self.__projZ + sCurr.getZ()))
            aNext = self.forcesCalculator(self.__dragCoeff1, a1, vCurr)
            vCurr = vector(vCurr.getX() + aNext.getX() * step,
                           vCurr.getY() + aNext.getY() * step,
                           vCurr.getZ() + aNext.getZ() * step)
            print("vCurr: " + str(vCurr))
            sCurr = point(sCurr.getX() + vCurr.getX() * step,
                          sCurr.getY() + vCurr.getY() * step,
                          sCurr.getZ() + vCurr.getZ() * step)

            #Data Grab
            tTotal = tTotal + self.__step
            self.__xArr.append(sCurr.getX())
            self.__yArr.append(sCurr.getY())
            self.__zArr.append(self.__projZ + sCurr.getZ())
            self.__zVelArr.append(vCurr.getZ())
            self.__zAccArr.append(aNext.getZ())
            self.__tArr.append(tTotal)

            #Debugging Print Statements
            if self.__debugPrintToggle:
                print("Current Altitude: " + str(self.__projZ + sCurr.getZ()))
                print("vCurr: " + str(vCurr))
                print("sCurr" + str(sCurr))

        while(abs(sCurr.getZ()) < self.__projZ):

            aNext = self.forcesCalculator(self.__dragCoeff2, a2 , vCurr)
            vCurr = vector(vCurr.getX() + aNext.getX() * step,
                           vCurr.getY() + aNext.getY() * step,
                           vCurr.getZ() + aNext.getZ() * step)

            sCurr = point(sCurr.getX() + vCurr.getX() * step,
                          sCurr.getY() + vCurr.getY() * step,
                          sCurr.getZ() + vCurr.getZ() * step)


            #Data Grab
            tTotal = tTotal + self.__step
            self.__xArr.append(sCurr.getX())
            self.__yArr.append(sCurr.getY())
            self.__zArr.append(self.__projZ + sCurr.getZ())
            self.__zVelArr.append(vCurr.getZ())
            self.__zAccArr.append(aNext.getZ())
            self.__tArr.append(tTotal)

            #Debugging Print Toggle
            # Debugging Print Statements
            if self.__debugPrintToggle:
                print("Current Altitude: " + str(self.__projZ + sCurr.getZ()))
                print("vCurr: " + str(vCurr))
                print("sCurr" + str(sCurr))

        return sCurr

    def dataOutput(self):
        if not self.__checkLoad:
            raise Exception("Data was not loaded. Run the drop calculator before accessing data")
        dataDump = [self.__xArr, self.__yArr, self.__zArr, self.__zVelArr, self.__zAccArr, self.__tArr]
        return dataDump

    def toggleDebug(self, status: bool):
        self.__debugPrintToggle = status
