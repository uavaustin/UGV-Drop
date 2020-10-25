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
from CartesianGeographicalConversions import *





"""
The dropCalclations class specifices the location and time? when a projectile should dropped to land on a target
    Input variables can be updated if not immediately known.
    Only one instance of this class is required to compute the drop location for a continous calculation of the drop spot.
    All units are in metric units: meters, kg, seconds, etc.

    Input Variables:
    @param velocityVector The velocity vector of the projectile.
    @param accelerationVector The acceleration vector of the projectile. NOTE: Add the acceleration in the Z direction NOT due to gravity
    @param projectileLoc The position of the projectile.
    @param targetLoc The position of the drop spot
    @param coeffOfDrag The drag coefficient of the parachute.
    @param dropProjSysMass The mass of the parachute, projectile system.
    @param parachuteArea The area of the parachute.
    @param parachuteDeploymentTime The time it takes to deploy the parachute.

TO USE THIS CLASS:
1. Create an instance with the properties of the projectile.
2. Update the position, velocity, and acceleration vectors every iteration.
3. Calculate the drop location using the calcDropSpot method every iteration.

"""
class dropCalculations:
    def __init__(self,
                velocityVector: vector,
                accelerationVector: vector,
                obsPoint: geoCord,
                originPoint: geoCord,
                coeffOfDrag: float,
                dropProjSysMass: float, #mass of parachute and UGV system
                parachuteArea: float,
                parachuteDeploymentTime: float):

        self.__translator = pointConversionTool(obsPoint, originPoint)
        projectileLoc = self.__translator.alignToOrigin(obsPoint)
        targetLoc = point(0, 0, 0)

        self.__dragCoeff = 1.0;
        if coeffOfDrag != 0:
            self.__dragCoeff = coeffOfDrag
        self.__mass = dropProjSysMass
        self.__g = -9.81 #acceleration due to gravity
        self.__airDensity = 1.225 #in kg/m^3
        self.__chuteArea = parachuteArea

        #Specific, derived values: Projectile Location
        self.__projX = projectileLoc.getX()
        self.__projY = projectileLoc.getY()
        self.__projZ = projectileLoc.getZ()

        #Specific, derived values: Target Location
        self.__tarX = targetLoc.getX()
        self.__tarY = targetLoc.getY()
        self.__tarZ = targetLoc.getZ()

        #velocities
        self.__vX = velocityVector.getX()
        self.__vY = velocityVector.getY()
        self.__vZ = velocityVector.getZ()
        self.__vZpost = 0 #velocity vector after chute has fully deployed

        #acceleration
        self.__aX = accelerationVector.getX()
        self.__aY = accelerationVector.getY()
        self.__aZ = accelerationVector.getZ()

        #Other Properties
        self.__chuteDepTime = parachuteDeploymentTime #chuteDepTime is the amount of time it takes for the chute to fully deploy

    def updateLocation(self, x: float, y: float, z: float):
        self.__projX = x
        self.__projY = y
        self.__projZ = z

    def updateVelocity(self, x: float, y: float, z: float):
        self.__vX = x
        self.__vY = y
        self.__vZ = z

    def updateAcceleration(self, x: float, y: float, z: float):
        self.__aX = x
        self.__aY = y
        self.__aZ = z

    def updateAirDensity(self, newDensity: float):
        self.__airDensity = newDensity

    def updateChuteDepTime(self, newDepTime: float):
        self.__chuteDepTime = newDepTime

    def calcDescentVelocity(self):
        if(self.__projZ == 0):
            raise Exception("\nHmmm. This function only works if the projectile is dropped in the air \nZ cannot be 0")
        velocity = 2*abs((self.__mass*self.__g))
        velocity = velocity/(self.__dragCoeff*self.__airDensity*self.__chuteArea)
        velocity = math.sqrt(velocity)
        self.__vZpost = -velocity
        print(self.__vZpost) #debugging

    def trueTimeToReachGround(self):
        s = (self.__vZ*self.__chuteDepTime) + (0.5)*(self.__g+self.__aZ)*(self.__chuteDepTime**2) #reflects vertical displacement during deployment
        remainingDistance = self.__projZ + s
        print(remainingDistance) #debugging
        self.calcDescentVelocity()
        newTime = abs(remainingDistance)/abs(self.__vZpost)
        print ("newTime/ true time: " + str(newTime)) #debugging
        return newTime

    def getDropDisplacementVector(self):
        time =  self.trueTimeToReachGround() + self.__chuteDepTime
        dep = self.__chuteDepTime
        print("chuteDepTime " + str(dep))
        print (str(time))
        xDisp = self.__vX*time + (0.5*self.__aX*(time**2))
        yDisp = self.__vY*time + (0.5*self.__aY*(time**2))
        zDisp = (self.__vZ*self.__chuteDepTime) + (0.5)*(self.__g+self.__aZ)*(self.__chuteDepTime**2)
        zDisp = zDisp + self.__vZpost*self.trueTimeToReachGround()
        print("zdisp c2 " + str(0.5*(self.__g+self.__aZ)*((self.trueTimeToReachGround()**2))))
        print("xdisp " + str(xDisp))
        print("ydisp " + str(yDisp))
        print("zdisp " + str(zDisp))
        dispVector = vector(xDisp, yDisp, zDisp)
        return dispVector

    #in retrospect not needed
    def calcLandSpot(self):
        theDispVector = self.getDropDisplacementVector()
        landPoint = point(self.__projX+theDispVector.getX(), self.__projY+theDispVector.getY(). self.__projZ+theDispVector.getZ())
        return landPoint

    def calcDropSpot(self):
        theDispVector = self.getDropDisplacementVector()
        dropXComp = self.__tarX - theDispVector.getX()
        dropYComp = self.__tarY - theDispVector.getY()
        dropZComp = self.__tarZ - theDispVector.getZ()
        currentDropSpot = point(dropXComp, dropYComp, dropZComp)
        return currentDropSpot

    def calcDropSpotGeoCord(self):
        pointF = self.calcDropSpot()
        output = self.__translator.pointToGeoCord(pointF)
        return output


"""
Debugging UI

"""

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
    ptD = geoCord(20.0001, 18.987, 0)

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


    deTest = dropCalculations(vAcc, vVe, ptP, ptD, 1.2, 6, 3.1928, 1)
    print(deTest.calcDropSpotGeoCord())

    stop = True
    """
    next = input("Stop?: ")
    if (next=="stop") or  (next=="STOP") :
        stop = True
    """


