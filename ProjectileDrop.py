"""
ProjectileDrop calculates the location at which a projectile needs to be dropped to reach an intended target.

Inputs: (complete later when done)
    Drag

Assumptions:
    The drone is moving at constant velocity.
    The projectile continues to move along the axis when it is dropped.

@author: rishthak

"""

import math

"""
----- dropProjectile NO LONGER NEEDED -----
The dropProjectile class contains the properties of the UGV projectile that is deployed from the UAV.
    @param xV The velocty of the UGV along the axis of the target.
    @param yV The velocity of the UGV perpendicular to the ground.
    @param mThe mass of the projecticle
    @param xA The acceleration of the UGV along the axis of the target. (This won't be used for now)
"""

class dropProjectile:
    def __init___(self, xV: float, yV: float, m: float, xA: float):
        self.xVelocity = xV
        self.yVelocity = yV
        self.mass = m
        self.xAcceleration = xA

    def getXV(self):
        return self.xVelocity

    def getYV(self):
        return self.yVelocity

    def getMass(self):
        return self.mass

    def getXA(self):
        return self.xAcceleration

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

    def setY(self, newZ: float):
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

    def getz(self):
        return self.z


""" (still working on it)
The computeDropLocation specifices the location and time? when a projectile should dropped to land on a target
    @param dropProj The object that will dropped of the dropProjectile class that specifies its properties
    @param projectileLoc The location of the dropProjectile. This will likely change with time and the class will account for that.
    @param targetLoc The location of the target
    @param coeffOfDrag The coefficient of drag. This value can be intialized upon creation or updated later.

"""

class dropCalculations:
    def __init__(self,
                velocityVector: vector,
                projectileLoc: point,
                targetLoc: point,
                coeffOfDrag: float,
                altitude: float,
                dropProjSysMass: float, #mass of parachute and UGV system
                parachuteArea: float):

        self.dragCoeff = 1.0;
        if coeffOfDrag != 0:
            self.dragCoeff = coeffOfDrag
        self.mass = dropProjMass
        self.g = 9.81 #acceleration due to gravity
        self.airDensity = 1.225 #in kg/m^3
        self.chuteArea = parachuteArea

        #Specific, derived values: Projectile Location
        self.projX = projectileLoc.getX();
        self.projY = projectileLoc.getY();
        self.projZ = projectileLoc.getZ();

        #Specific, derived values: Target Location
        self.tarX = targetLoc.getX();
        self.tarY = targetLoc.getY();
        self.tarZ = targetLoc.getZ();

        #velocities
        self.vX = veloctyVector,getX();
        self.vY = veloctyVector.getY();
        self.vZ = veloctyVector.getZ();
        self.vYpost = 0 #velocity vector after chute is deployed

        #Other Properties
        self.chuteDepTime = 0.00 #chuteDepTime is the amount of time it takes for the chute to fully deploy

    def updateLocation(x: float, y: float, z: float):
        self.projX = x
        self.projY = y
        self.projZ = z

    def updateVelocity(x: float, y: float, z: float):
        self.xV = x
        self.yV = y
        self.zV = z

    def updateAirDensity(newDensity: float):
        self.airDensity = newDensity

    def calcDescentVelocity(self):
        velocity = 2*(mass*g)
        velocity = velocity/(self.dragCoeff*self.airDensity*self.chuteArea)
        velocity = math.sqrt(velocity)
        self.vYpost = velocity

    def trueTimeToReachGround(self):
        #reflects vertical displacement during deployment
        s = (self.yV*self.deploymentTime) + (0.5)*(self.g)*(self.deploymentTime**2)
        remainingDistance = self.projY - s
        self.calcDescentVelocity()
        newTime = math.abs(remainingDistance)/math.abs(self.vYpost)
        return newTime

    def getDropDisplacementVector(self):
        time =  self.trueTimeToReachGround()
        xDisp = self.vX*time
        yDisp = -self.getY() #assumption: my calculations above are correct
        zDisp = self.vZ*time
        dispVector = vector(xDisp, yDisp, zDisp)
        return dispVector

    #in retrospect not needed
    def calcLandSpot(self):
        dispVector = self.getDropDisplacementVector()
        landPoint = point(self.projX+dispVector.getX(), self.projY+dispVector.getY(). self.projZ+dispVector.getZ())
        return landPoint

    def calcDropSpot(self):
        dispVector = self.getDropDisplacementVector
        dropXComp = self.tarX - dispVector.getX()
        dropYComp = self.tarY
        dropZComp = self.tarZ - dispVector.getZ()
        currentDropSpot = point(dropXComp, dropYComp, dropZComp)
        return currentDropSpot
