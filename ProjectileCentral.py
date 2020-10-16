"""
The ProjectileCentral file is the centralized location where the
UGV projectile management is getDropDisplacementVector

Files needed: ProjectileLocation.py and ProjectileDrop.py

@author rishthak

"""

from ProjectileDrop import *
import math

"""
Location of Projectile
"""
obsPoint = pointLatLon(0,0,0)


"""
Location of Drop Spot
"""
originPoint = pointLatLon(0,0,0)

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
translator = alignToOriginTool(obsPoint, originPoint)
obsPointCart = translator.alignToOrigin(obsPoint)
orgPointCart = point (0,0,0)
dropCalculator = dropCalculations(veAcc, veAcc, obsPointCart, orgPointCart, chuteDragCoeff, systemMass, chuteArea, chuteDeployTime)
print(dropCalculator.calcDropSpot())
