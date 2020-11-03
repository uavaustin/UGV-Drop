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
from CartGeoConversions import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt





"""
The dropCalclations class specifices the location and time? when a projectile should dropped to land on a target
    Input variables can be updated if not immediately known.
    Only one instance of this class is required to compute the drop location for a continous calculation of the drop spot.
    All units are in metric units: meters, kg, seconds, etc.

    Input Variables:
     @param velocityVector      The initial velocity of the projectile
     @param currentAltitude     The current altitude of the projectile
     @param targetPoint         The location of the target
     @param coeffOfDragPhase1   The coefficient of drag during phase 1
     @param coeffOfDragPhase2   The coefficient of drag during phase 2
     @param dropProjSysMass     The mass of the system
     @param systemArea1         The area of the projectile in phase 1
     @param systemArea2         The area of the projectile in phase 2
     @param airDensity          The density of the air
     @param step                The time step for the solver
     @param deploymentHeight    The height at which phase 2 is initiated
    

TO USE THIS CLASS:
1. Create an instance with the properties of the projectile.
2. Update the position, velocity, and acceleration vectors every iteration.
3. Calculate the drop location using the calcDropSpot method every iteration.

"""
class dropCalculations:
    def __init__(self,
                velocityVector: vector,
                currentAltitude: float,
                targetPoint: geoCord,
                coeffOfDragPhase1: float,
                coeffOfDragPhase2: float,
                dropProjSysMass: float, #mass of parachute and UGV system
                systemArea1: float,
                systemArea2: float,
                airDensity: float,
                deploymentHeight: float,
                step: float ):


        #Phase 1 Phase 2 Drag Coefficients
        self.__dragCoeff1 = coeffOfDragPhase1
        self.__dragCoeff2 = coeffOfDragPhase2

        #Fixed Constants
        self.__mass = dropProjSysMass
        self.__g = -9.81 #acceleration due to gravity
        self.__airDensity = airDensity #in kg/m^3
        self.__sysA1 = systemArea1
        self.__sysA2 = systemArea2


        #  Locations in Cartesian
        self.__projZ = currentAltitude

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
        output = cartGeoConv.alignToOrgin(coordinate, self.__targetGeo)
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
                           vCurr.getY() + aNext.getY() * step,
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
            xArr.append(sCurr.getX())
            yArr.append(sCurr.getY())
            zArr.append(self.__projZ+sCurr.getZ())
            plt.figure(4)
            plt.scatter(tTotal, aNext.getZ(), c = 'green')

        while(abs(sCurr.getZ()) < self.__projZ):

            print("Current Altitude: " + str(self.__projZ + sCurr.getZ()))
            aNext = self.forcesCalculator(self.__dragCoeff2, a2 , vCurr)
            vCurr = vector(vCurr.getX() + aNext.getX() * step,
                           vCurr.getY() + aNext.getY() * step,
                           vCurr.getZ() + aNext.getZ() * step)

            sCurr = point(sCurr.getX() + vCurr.getX() * step,
                          sCurr.getY() + vCurr.getY() * step,
                          sCurr.getZ() + vCurr.getZ() * step)


            #Data Analysis
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
            xArr.append(sCurr.getX())
            yArr.append(sCurr.getY())
            zArr.append(self.__projZ + sCurr.getZ())
            plt.figure(4)
            plt.scatter(tTotal, aNext.getZ(), c='green')
            plt.xlabel("Time")
            plt.ylabel("Acceleration")

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
    #ptP = geoCord(20.000, 18.777, 20)

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

    deTest = dropCalculations(vVe, 20, ptD, 1.2, 2.4, 6, 1.1928, 4.1928, 1.225, 17.0, 0.01)
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


#Everything Below is for the Data Visualization
fig = plt.figure(2)
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.scatter3D(xArr, yArr, zArr, c='r', marker='o')

def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = numpy.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = numpy.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = numpy.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

set_axes_equal(ax)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.figure(5)
newViewX = numpy.array(xArr)**2
newViewY = numpy.array(yArr)**2
newThatView = newViewX+newViewY
newThatView = numpy.array(newThatView**(1/2))
finalBaseAxis = newThatView.tolist()
plt.scatter(finalBaseAxis, zArr)
plt.xlabel("Side View Axis?")
plt.axis('equal')
plt.ylabel("Altitude")

plt.show()

#position, velocity, acceleration, with respect to time
# 2-5x area and coefficient drag