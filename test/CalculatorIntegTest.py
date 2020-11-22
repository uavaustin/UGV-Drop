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
    zV = random.uniform(0, 20.0)
    alt = random.uniform(10,100)
    dragP1 = random.uniform(1.01, 2)
    dragP2 = random.uniform(dragP1, 4)
    mass = random.uniform(3, 15)
    systemArea1 = random.uniform(1, 3)
    systemArea2 = random.uniform(systemArea1, 5)
    airDensity = 1.225
    deploymentHeight = random.uniform(alt/3, alt/1.01)
    step = 0.01


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
    print("New Test \n")
    if rapid is False:
        input("Not yet set")
    else:
        print("xV: " + str(xV))
        input("Continue")
        print("Net Disp: " + str(dropCalculator.calcDropSpot()))
        print("Drop Loc: " + str(dropCalculator.calcDropSpotGeoCord()))
        input("Continue")
    
    #Decrement
    i = i - 1