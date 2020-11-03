"""
The DropCalculatorManager class is where the calculations pertaining to the UGV Drop are handled.
All inputs are specified below in a standardized format. At the moment, the result is outputted in
the terminal.

Files Needed:
 src folder containing (__init__.py, CartesianCoordinate.py, CartGeoConversions.py,

Note: Projectile and UGV is used interchangeably though both terms represent the UGV.

@author rishthak

"""

from src import *
import math

"""

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
"""

"""
The current velocity of the projectile in all three dimensions, expressed as a vector
"""
originPoint = geoCord(20.000,17.778,0)

"""
Velocity Vector
"""
veVel = vector(5,5,0)

"""
Acceleration Vector
"""
veAcc= vector(0.5,0.5,0.002)

"""
Projectile Properties
"""
systemMass = 1.000
chuteArea = 1.000
chuteDragCoeff = 1.200
chuteDeployTime = 2.500

"""
Computation
"""

dropCalculator = dropCalculations(veAcc, veAcc, obsPointCart, orgPointCart, chuteDragCoeff, systemMass, chuteArea, chuteDeployTime)
print(dropCalculator.calcDropSpot())
