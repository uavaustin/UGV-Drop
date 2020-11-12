"""
The GeoIntegTest class integration tests the Geographical Outputs

@risthak

"""
import math
import numpy
from src.DropCalculator import dropCalculations
from src.CartesianVector import vector
from src.CartesianCoordinate import point
from src.GeographicalCoordinate import geoCord
from src.CartGeoConversions import cartGeoConv
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
#rom mpl_toolkits.basemap import Basemap


def pullGeoData(dropCalcSet: [], dropGeoCord: geoCord):
    xArr = dropCalcSet[0]
    yArr = dropCalcSet[1]
    zArr = dropCalcSet[2]
    tArr = dropCalcSet[5]
    lat = []
    lon = []
    alt = []
    translator = cartGeoConv()
    i = 0
    while(i < tArr.length()):
            pointObs = point(xArr[i], yArr[i], zArr[i])
            pullPoint = translator.alignToOrgin(pointObs, dropGeoCord)
            lat.append(pullPoint.getLat())
            lon.append(pullPoint.getLon())
            alt.append(pullPoint.getAlt())
            i = i+1
    return [lat, lon, alt]

#Testing
dropCalculator = dropCalculations(vector(2, 2, 0.002), 20, geoCord(20.0001, 18.778, 0) , 1.2, 2.4, 6, 1.1928, 4.1928, 1.225, 17.0, 0.01)
output = dropCalculator.calcDropSpotGeoCord()
cartDataPull = dropCalculator.dataOutput()
geoDataPull = (cartDataPull, geoCord)
print(geoDataPull)