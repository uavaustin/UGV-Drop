"""
The ProjectileDrop calculates the location at which a projectile needs to be dropped to reach an intended target.

Inputs:
    * Drag Coefficient of the Parachute
    * Air Density
    * The Position Vector of the UGV (Projectile)
    * The Velocity Vector of the UGV (Projectile)
    * The Acceleration Vector of the UGV (Projectile)

Assumptions:
    The coefficient of drag for parachute is known.
    The Projectile vertically when during the time the chute is being deployed.

@author: rishthak

"""

import math

"""
The point class specifies a point in three dimensions
    @param xComp The X Component running laterally to the ground
    @param xComp The Y Component perpendicular to the ground. The ground is presumed to be 0
    @param xComp The Z Component longitudinal to the ground

"""
class point:
    def __init__(self, xComp: float, yComp: float, zComp: float):
        self.x = xComp
        self.y = yComp
        self.z = zComp
    def __str__(self):
        return ("X: "  + str(self.x) + " Y: " + str(self.y) + " Z: " + str(self.z))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def setX(self, newX: float):
        self.x = newX

    def setY(self, newY: float):
        self.y = newY

    def setZ(self, newZ: float):
        self.z = newZ

"""
The vector class specifies a vector in three dimensions
    @param xComp The X Component running laterally to the ground
    @param xComp The Y Component perpendicular to the ground. The ground is presumed to be 0
    @param xComp The Z Component longitudinal to the ground

"""
class vector:
    def __init__(self, xComp: float, yComp: float, zComp: float):
        self.x = xComp
        self.y = yComp
        self.z = zComp

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

"""
The dropCalclations class specifices the location and time? when a projectile should dropped to land on a target
    Input varaibles can be updated if not immediately known.
    Only one instance of this class is required to compute the drop location for a continous calculation of the drop spot.
    All units are in metric units: meters, kg, seconds, etc.

    Input Variables:
    @param velocityVector The velocity vector of the projectile.
    @param accelerationVector The acceleration vector of the projectile. NOTE: Add the acceleration in the Y direction NOT due to gravity
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
                projectileLoc: point,
                targetLoc: point,
                coeffOfDrag: float,
                dropProjSysMass: float, #mass of parachute and UGV system
                parachuteArea: float,
                parachuteDeploymentTime: float):

        self.dragCoeff = 1.0;
        if coeffOfDrag != 0:
            self.dragCoeff = coeffOfDrag
        self.mass = dropProjSysMass
        self.g = -9.81 #acceleration due to gravity
        self.airDensity = 1.225 #in kg/m^3
        self.chuteArea = parachuteArea

        #Specific, derived values: Projectile Location
        self.projX = projectileLoc.getX()
        self.projY = projectileLoc.getY()
        self.projZ = projectileLoc.getZ()

        #Specific, derived values: Target Location
        self.tarX = targetLoc.getX()
        self.tarY = targetLoc.getY()
        self.tarZ = targetLoc.getZ()

        #velocities
        self.vX = velocityVector.getX()
        self.vY = velocityVector.getY()
        self.vZ = velocityVector.getZ()
        self.vYpost = 0 #velocity vector after chute has fully deployed

        #acceleration
        self.aX = accelerationVector.getX()
        self.aY = accelerationVector.getY()
        self.aZ = accelerationVector.getZ()

        #Other Properties
        self.chuteDepTime = parachuteDeploymentTime #chuteDepTime is the amount of time it takes for the chute to fully deploy

    def updateLocation(self, x: float, y: float, z: float):
        self.projX = x
        self.projY = y
        self.projZ = z

    def updateVelocity(self, x: float, y: float, z: float):
        self.vX = x
        self.vY = y
        self.vZ = z

    def updateAcceleration(self, x: float, y: float, z: float):
        self.aX = x
        self.aY = y
        self.aZ = z

    def updateAirDensity(self, newDensity: float):
        self.airDensity = newDensity

    def updateChuteDepTime(self, newDepTime: float):
        self.chuteDepTime = newDepTime

    def calcDescentVelocity(self):
        velocity = 2*abs((self.mass*self.g))
        velocity = velocity/(self.dragCoeff*self.airDensity*self.chuteArea)
        velocity = math.sqrt(velocity)
        self.vYpost = -velocity
        print(self.vYpost) #debugging

    def trueTimeToReachGround(self):
        s = (self.vY*self.chuteDepTime) + (0.5)*(self.g+self.aY)*(self.chuteDepTime**2) #reflects vertical displacement during deployment
        remainingDistance = self.projY + s
        print(remainingDistance) #debugging
        self.calcDescentVelocity()
        newTime = abs(remainingDistance)/abs(self.vYpost)
        print ("newTime/ true time: " + str(newTime)) #debugging
        return newTime

    def getDropDisplacementVector(self):
        time =  self.trueTimeToReachGround() + self.chuteDepTime
        dep = self.chuteDepTime
        print("chuteDepTime " + str(dep))
        print (str(time))
        xDisp = self.vX*time + (0.5*self.aX*(time**2))
        yDisp = (self.vY*self.chuteDepTime) + (0.5)*(self.g+self.aY)*(self.chuteDepTime**2)
        yDisp = yDisp + self.vYpost*self.trueTimeToReachGround()
        print("ydisp c2 " + str(0.5*(self.g+self.aY)*((self.trueTimeToReachGround()**2))))
        zDisp = self.vZ*time + (0.5*self.aZ*(time**2))
        print("xdisp " + str(xDisp))
        print("ydisp " + str(yDisp))
        print("zdisp " + str(zDisp))
        dispVector = vector(xDisp, yDisp, zDisp)
        return dispVector

    #in retrospect not needed
    def calcLandSpot(self):
        theDispVector = self.getDropDisplacementVector()
        landPoint = point(self.projX+theDispVector.getX(), self.projY+theDispVector.getY(). self.projZ+theDispVector.getZ())
        return landPoint

    def calcDropSpot(self):
        theDispVector = self.getDropDisplacementVector()
        dropXComp = self.tarX - theDispVector.getX()
        dropYComp = self.tarY - theDispVector.getY()
        dropZComp = self.tarZ - theDispVector.getZ()
        currentDropSpot = point(dropXComp, dropYComp, dropZComp)
        return currentDropSpot



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
    ptP = point(20, 20, 20)

    """
    xDi = input("\n X Component of Position (DropSpot): ")
    yDi = input("\n Y Component of Position (DropSpot): ")
    zDi = input("\n Z Component of Position (DropSpot): ")
    ptD = point(xDi, yDi, zDi)
    """
    ptD = point(15, 0, 21)

    """
    xDi = input("\n X Component of Velocity (Projectile): ")
    yDi = input("\n Y Component of Velocity (Projectile): ")
    zDi = input("\n Z Component of Velocity (Projectile): ")
    vVe = vector(xDi, yDi, zDi)
    """
    vVe = vector(2, 0.002, 2)


    """
    xDi = input("\n X Component of Acceleration (Projectile): ")
    yDi = input("\n Y Component of Acceleration (Projectile): ")
    zDi = input("\n Z Component of Acceleration (Projectile): ")
    vAcc = vector(xDi, yDi, zDi)
    """
    vAcc = vector(0.5, 0, 0.5)


    deTest = dropCalculations(vAcc, vVe, ptP, ptD, 1.2, 6, 3.1928, 1)
    print(deTest.calcDropSpot())

    stop = True
    """
    next = input("Stop?: ")
    if (next=="stop") or  (next=="STOP") :
        stop = True
    """
