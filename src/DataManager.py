"""
The DataManager class handles the data management for the dropCalculator. Specifically, it can produces various graphs
based on the data output by the dropCalculator.

@author rishthak
"""

#TBD
import math
import time
import numpy
from DropCalculator import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

class manageDropData:
    def __init__(self,
                xArray: [],
                yArray: [],
                zArray: [],
                zVelArray: [],
                zAccArray: [],
                tArray: [])

        #Define Arrays
        self.__xArr = xArray
        self.__yArr = yArray
        self.__zArr = zArray
        self.__zVelArr = zVelArray
        self.__zAccArr = zAccArray
        self.__tArr = tArray

    def buildAltChart(self):
        plt.figure(1)
        plt.scatter(tArray, zArray)
        plt.xlabel("Time")
        plt.ylabel("Altitude")

    def buildVelChart(self):
        plt.figure(2)
        plt.scatter(tArray, zArray)
        plt.xlabel("Time")
        plt.ylabel("Altitude")

    def buildVelChart(self):
        plt.figure(2)
        plt.scatter(tArray, zArray)
        plt.xlabel("Time")
        plt.ylabel("Altitude")

