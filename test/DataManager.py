"""
The DataManager class handles the data management for the dropCalculator. Specifically, it can produces various graphs
based on the data output by the dropCalculator.

The DataManager class needs to import the following files and respective classes:
                        math
                        numpy
                        DropCalculator: dropCalculations
                        GeographicalCoordinate: geoCord
                        CartesianVector:  vector
                        mpl_toolkits: mplot3d
                        matplotlib: pyplot as plt

@author rishthak
"""

#TBD
import math
import numpy
from src.DropCalculator import dropCalculations
from src.GeographicalCoordinate import geoCord
from src.CartesianVector import vector
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap

"""
The dropDataManager class is used to create and display graphs from the DropCalculator data. This class works in
conjunction with DropCalculator.

The class supports 5 types of data display:
    * Altitude vs Time
    * Velocity vs Time
    * Acceleration vs Time
    * A 3D chart showing the projectile's displacement in all three directions.
    * A chart showing the projectile's directly perpendicular to the axis of it's motion. (Inappropriately labeled as 
      buildAlongAxis below)
      
    *** Special Thanks to "karlo" from StackExchange on creating a method for equalizing the axises of the 3d graph
        in matplotlib ***

@param dropCalcSet The data loaded in from the drop calculations. 

"""
class dropDataManager:
    def __init__(self,dropCalcSet: []):

        #Data Arrays are Defined
        self.__xArr = dropCalcSet[0]
        self.__yArr = dropCalcSet[1]
        self.__zArr = dropCalcSet[2]
        self.__zVelArr = dropCalcSet[3]
        self.__zAccArr = dropCalcSet[4]
        self.__tArr = dropCalcSet[5]

    def buildAltChart(self):
        plt.figure(1)
        plt.scatter(self.__tArr, self.__zArr, c='r', marker='o')
        plt.xlabel("Time")
        plt.ylabel("Altitude")

    def buildVelChart(self):
        plt.figure(2)
        plt.scatter(self.__tArr, self.__zVelArr, c='g', marker='o')
        plt.xlabel("Time")
        plt.ylabel("Velocity")

    def buildAccChart(self):
        plt.figure(3)
        plt.scatter(self.__tArr, self.__zAccArr, c='b', marker='o')
        plt.xlabel("Time")
        plt.ylabel("Acceleration")
        plt.plot([0, self.__tArr[-1]], [-9.81, -9.81], color='k', linestyle='-', linewidth=2)

    def build3DPlot(self):
        plt.figure(4)
        fig = plt.figure(4)
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        ax.scatter3D(self.__xArr, self.__yArr, self.__zArr, c='c', marker='o')
        self.set_axes_equal(ax)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

    def buildAlongAxis(self):
        plt.figure(5)
        nX = numpy.array(self.__xArr) ** 2
        nY = numpy.array(self.__yArr) ** 2
        nAx = nX + nY
        nAx = numpy.array(nAx ** (1 / 2))
        finalBaseAxis = nAx.tolist()
        plt.scatter(finalBaseAxis, self.__zArr, c='m', marker='o')
        plt.xlabel("Along Axis of Motion")
        plt.ylabel("Altitude")
        plt.axis('equal')

    def buildAll(self):
        self.buildAltChart()
        self.buildVelChart()
        self.buildAccChart()
        self.build3DPlot()
        self.buildAlongAxis()

    def showData(self):
        plt.show()

    def deBUG(self):
        self.buildAccChart()

    #Credit to "karlo" on StackExchange that made this method to make the 3d axises symmetrical
    def set_axes_equal(self, ax):
        '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
        cubes as cubes, etc..  This is one possible solution to Matplotlib's
        ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

        Input
          ax: a matplotlib axis, e.g., as output from plt.gca().
        '''

        x_limits = ax.get_xlim3d()
        y_limits = ax.get_ylim3d()
        z_limits = ax.get_zlim3d()

        x_range = abs(x_limits[1] - x_limits[0])
        x_middle = numpy.mean(x_limits)
        y_range = abs(y_limits[1] - y_limits[0])
        y_middle = numpy.mean(y_limits)
        z_range = abs(z_limits[1] - z_limits[0])
        z_middle = numpy.mean(z_limits)

        # The plot bounding box is a sphere in the sense of the infinity
        # norm, hence I call half the max range the plot radius.
        plot_radius = 0.5 * max([x_range, y_range, z_range])

        ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
        ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
        ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

"""
Functionality Check
"""
"""
ptD = geoCord(20.0001, 18.778, 0)
vVe = vector(2, 2, 0.002)
vAcc = vector(0.5, 0.5, 0)
dropCalc = dropCalculations(vVe, 20, ptD, 1.2, 2.4, 6, 1.1928, 4.1928, 1.225, 17.0, 0.01)
print(dropCalc.calcDropSpotGeoCord())
manager = dropDataManager(dropCalc.dataOutput())
manager.buildAll()
manager.showData()
"""
