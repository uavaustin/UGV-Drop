"""
The DropCalculatorManager class is where the calculations pertaining to the UGV Drop are handled.
All inputs are specified below in a standardized format. At the moment, the result is outputted in
the terminal.

Files Needed:
 src folder containing (__init__.py,
                        CartesianCoordinate.py,
                        CartesianVector.py,
                        CartGeoConversions.py,
                        DropCalculator.py,
                        GeographicalCoordinate.py,
                        DataManager.py )


Note: Projectile and UGV is used interchangeably though both terms represent the UGV.

@author rishthak

"""

from src.DropCalculator import dropCalculations
from src.GeographicalCoordinate import geoCord
from src.CartesianVector import vector
from test.DataManager import dropDataManager

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


deTest = dropCalculations(vVe, 20, ptD, 1.2, 2.4, 6, 1.1928, 4.1928, 1.225, 0.01, 17)
"""

"""
velV: The current velocity of the projectile in all three dimensions, expressed as a vector.
"""
velV = vector(2,2,0.002)

"""
currAlt: The current altitude of the projectile in meters, expressed as a float.
"""
currAlt = 20.0

"""
tarP: The current location of the UGV target in degrees, expressed as a geographical coordinate
"""
tarP = geoCord(20.000,17.778,0)

"""
coeff1: The coefficient of drag in the first phase, expressed as a float.
"""
coeff1 = 1.2

"""
coeff2: The coefficient of drag in the first phase, expressed as a float.
"""
coeff2 = 2.4

"""
sysMass: The mass of the projectile in kilograms, expressed as a float.
"""
sysMass = 6

"""
sysArea1: The surface area of the projectile system during phase 1 in meters squared, expressed as a float.
"""
sysArea1 = 1.1928

"""
sysArea2: The surface area of the projectile system during phase 2 in meters squared, expressed as a float.
"""
sysArea2 = 4.1928

"""
airDens: The density of the air in which the projectile is falling in kilograms per meter squared, expressed as a float.
"""
airDens = 1.225

"""
phase2Alt: The altitude at which successful chute deployment occurs at the projectile enters phase 2 in meters, expressed as a float.
"""
phase2Alt = 17

"""
step: The time step for the forces solver in the drop calculator in seconds, expressed as a float.
"""
step = 0.01

"""
Actual Calculations
"""
dropCalculator = dropCalculations(velV,
                          currAlt,
                          tarP,
                          coeff1,
                          coeff2,
                          sysMass,
                          sysArea1,
                          sysArea2,
                          airDens,
                          phase2Alt,
                          step)
output = dropCalculator.calcDropSpotGeoCord()
dataPull = dropCalculator.dataOutput()

"""
Data Outputs. Make sure a calcDropSpotGeoCord() or calcDropSpot() method is called to load the data.
"""
manager = dropDataManager(dataPull)
manager.buildAll()
manager.showData()

"""
Toggle Print Outputs to Debug Data
"""








