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
        print(theDispVector)
        dropXComp = 0 - theDispVector.getX()
        dropYComp = 0 - theDispVector.getY()
        dropZComp = 0 - theDispVector.getZ()
        currentDropSpot = point(dropXComp, dropYComp, dropZComp)
        print(currentDropSpot)
        return currentDropSpot

    def calcDropSpotGeoCord(self):
        coordinate = self.calcDropSpot()
        output = self.__translator.pointToOrgS(coordinate, self.__targetGeo)
        return output

    def forcesCalculator(self, dragCoeff: float, surfaceArea: float, vThisStep: vector):
        print("step")
        aX = (-1*numpy.sign(self.__vX))*((.5)*self.__airDensity*dragCoeff*surfaceArea*(vThisStep.getX()**2))/self.__mass
        aY= (-1*numpy.sign(self.__vY))*((.5)*self.__airDensity*dragCoeff*surfaceArea*(vThisStep.getY()**2))/self.__mass
        aZ = self.__g + ((.5)*self.__airDensity*dragCoeff*surfaceArea*(vThisStep.getZ()**2))/self.__mass

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
                           vCurr.getY() + aNext.getX() * step,
                           vCurr.getZ() + aNext.getZ() * step)
            print("vCurr: " + str(vCurr))
            sCurr = point(sCurr.getX() + vCurr.getX() * step,
                          sCurr.getY() + vCurr.getY() * step,
                          sCurr.getZ() + vCurr.getZ() * step)

            #Debugging and Data Analysis
            tTotal = tTotal + self.__step
            plt.figure(0)
            plt.scatter(tTotal, self.__projZ+sCurr.getZ(), c = 'red')
            plt.figure(1)
            plt.scatter(tTotal, vCurr.getZ(), c='blue')
            print("sCurr" + str(sCurr))
            xArr.append(self.__projX+sCurr.getX())
            yArr.append(self.__projY+sCurr.getY())
            zArr.append(self.__projZ+sCurr.getZ())

        while(abs(sCurr.getZ()) < self.__projZ):

            print("Current Altitude: " + str(self.__projZ + sCurr.getZ()))
            aNext = self.forcesCalculator(self.__dragCoeff2, a2 , vCurr)
            vCurr = vector(vCurr.getX() + aNext.getX() * step,
                           vCurr.getY() + aNext.getY() * step,
                           vCurr.getZ() + aNext.getZ() * step)

            sCurr = point(sCurr.getX() + vCurr.getX() * step,
                          sCurr.getY() + vCurr.getY() * step,
                          sCurr.getZ() + vCurr.getZ() * step)


            print("vCurr: " + str(vCurr))
            print("sCurr" + str(sCurr))
            tTotal = tTotal + self.__step
            plt.figure(0)
            plt.scatter(tTotal, self.__projZ + sCurr.getZ(), c='red')
            plt.xlabel("Time")
            plt.ylabel("Altitude")
            plt.figure(1)
            plt.scatter(tTotal, vCurr.getZ(), c='blue')
            plt.xlabel("Time")
            plt.ylabel("Velocity")
            xArr.append(self.__projX + sCurr.getX())
            yArr.append(self.__projY + sCurr.getY())
            zArr.append(self.__projZ + sCurr.getZ())


        return sCurr








"""
Debugging UI

"""
xArr = []
yArr = []
zArr = []

stop = False
while stop!=True:
    """
    xDi = input("\n X Component of Position (Projectile): ")
    yDi = input("\n Y Component of Position (Projectile): ")
    zDi = input("\n Z Component of Position (Projectile): ")
    ptP = point(xDi, yDi, zDi)
    """
    ptP = geoCord(20.000, 18.777, 20)

    """
    xDi = input("\n X Component of Position (DropSpot): ")
    yDi = input("\n Y Component of Position (DropSpot): ")
    zDi = input("\n Z Component of Position (DropSpot): ")
    ptD = point(xDi, yDi, zDi)
    """
    ptD = geoCord(20.0001, 18.778, 0)

    """
    xDi = input("\n X Component of Velocity (Projectile): ")
    yDi = input("\n Y Component of Velocity (Projectile): ")
    zDi = input("\n Z Component of Velocity (Projectile): ")
    vVe = vector(xDi, yDi, zDi)
    """
    vVe = vector(2, 2, 0.002)


    """
    xDi = input("\n X Component of Acceleration (Projectile): ")
    yDi = input("\n Y Component of Acceleration (Projectile): ")
    zDi = input("\n Z Component of Acceleration (Projectile): ")
    vAcc = vector(xDi, yDi, zDi)
    """
    vAcc = vector(0.5, 0.5, 0)

    deTest = dropCalculations(vVe, ptP, ptD, 1.2, 1.2, 6, 1.1928, 1.1928, 1.225, 0.01, 17)
    print(deTest.calcDropSpotGeoCord())

    stop = True
    """
    next = input("Stop?: ")
    if (next=="stop") or  (next=="STOP") :
        stop = True 
    """
#debugTranslator = pointConversionTool(ptP, ptD)
#print("post\n")
#transP = point(4, 4, 0)
#print(debugTranslator.pointToOrgS(transP, ptD))

fig = plt.figure(2)
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.scatter3D(xArr, yArr, zArr, c='r', marker='o')

plt.show()