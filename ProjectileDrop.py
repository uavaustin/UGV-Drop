"""
ProjectileDrop calculates the location at which a projectile needs to be dropped to reach an intended target.

Inputs: (complete later when done)
    Drag

Assumptions:
    The drone is moving along the axis of the intended target.
    The drone is moving at constant velocity.
    The projectile continues to move along the axis when it is dropped.

@author: rishthak

"""

"""
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
The pointLocation class specifies a point in three dimensions
    @param xComp The X Component running laterally to the ground
    @param xComp The Y Component perpendicular to the ground. The ground is presumed to be 0
    @param xComp The Z Component longitudinal to the ground

"""
class pointLocation:
    def __init__(self, xComp: float, yComp: float, zComp: float):
        self.x = xComp
        self.y = yComp
        self.z = zComp

    def getX():
        return self.x

    def getY():
        return self.y

    def getz():
        return self.z

""" (still working on it)
The computeDropLocation specifices the location and time? when a projectile should dropped to land on a target
    @param dropProj The object that will dropped of the dropProjectile class that specifies its properties
    @param projectileLoc The location of the dropProjectile. This will likely change with time and the class will account for that.
    @param targetLoc The location of the target
    @param coeffOfDrag The coefficient of drag. This value can be intialized upon creation or updated later.

"""

class computeDropLocation:
    def __init__(self,
                dropProj: dropProjectile,
                projectileLoc: pointLocation,
                targetLoc: pointLocation,
                coeffOfDrag: float):
        self.dropProjectile = proj
        self.projLoc = projLoc
        self.tarLoc = tarLoc
        self.dragCoeff = 0;
        if coeffOfDrag != 0:
            self.dragCoeff = coeffOfDrag

        #Specific, derived values: Projectile Location
        self.projX = self.projectileSpot.getX();
        self.projY = self.projectileSpot.getY();
        self.projZ = self.projectileSpot.getZ();

        #Specific, derived values: Target Location
        self.tarX = self.tarLoc.getX();
        self.tarY = self.tarLoc.getY();
        self.tarZ = self.tarLoc.getZ();

    def updateLocation(self):
        return

    def currentDistance(self):
        return

    def timeToReachGround(self):
        return

    def dragFactor(self):
        return

    def trueTimeToReachGround(self):
        return

    def calcDropLoc(self):
        return
