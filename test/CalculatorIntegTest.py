"""
This class is designed to integration test the functionality of the Drop Calculator

@author: rishthak

"""

from src.DropCalculator import dropCalculations
from src.CartesianVector import vector
from src.GeographicalCoordinate import geoCord
import numpy
import matplotlib
import random
from DataManager import dropDataManager

#
i=20
rapid = True

while (i > 0):
    
    #Build a Random Test
    xV = random.uniform(0, 20.0)
    yV = random.uniform(0, 20.0)
    zV = random.uniform(1,5)  #Problematic
    alt = random.uniform(10,100)
    dragP1 = random.uniform(0, 2)
    dragP2 = random.uniform(dragP1, 4)
    mass = random.uniform(3, 15)
    systemArea1 = random.uniform(1, 3)
    systemArea2 = random.uniform(systemArea1, 5)
    airDensity = 1.225
    deploymentHeight = random.uniform(alt/3, alt/1.01)
    step = 1

    
    dropCalculator = dropCalculations(vector(xV, yV, zV), 
                                            alt, 
                                            geoCord(38.272790, -76.433341, 0), 
                                            dragP2, 
                                            dragP2, 
                                            mass, 
                                            systemArea1, 
                                            systemArea2, 
                                            airDensity, 
                                            deploymentHeight, 
                                            step)
    dropCalculator.toggleDebug(True)
    
    print("New Test \n")
    if rapid is False:
        input("Not yet set")
    else:
        print("vVector: " + str(vector(xV, yV, zV)))
        print("airDensity: " + str(airDensity))
        print("alt: " + str(alt))
        print("deploymentHeight: " + str(deploymentHeight))
        print("dragP1 " + str(dragP1))
        print("dragP2: " + str(dragP2))
        print("mass: " + str(mass))
        print("systemArea1: " + str(systemArea1))
        print("systemArea2: " + str(systemArea2))
        print("airDensity: " + str(airDensity))

        input("Continue")
        print("Net Disp: " + str(dropCalculator.calcDropSpot()))
        print("Drop Loc: " + str(dropCalculator.calcDropSpotGeoCord()))
        input("Continue")
    
    #Decrement
    i = i - 1