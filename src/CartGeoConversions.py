"""
The CartGeoConversions converts cartesian information into a geographical coordinate based on a specified origin.

@author: rishthak, jordan

"""
import math
from CartesianCoordinate import *
from CartesianVector import *
from GeographicalCoordinate import *

"""
The alignToOriginTool can be used to translate a geoCord to a point at a specified origin. This method is observation
location independent. In other words, you just need to know how far the projectile will drop, not where it is.
    @param observationPoint The geoCord defined as the final position of the projectile if it were to drop based on the
        calculated drop displacement vector and land at (0, 0, 0,).
        NOTE: This DOES NOT treat the projectile as the origin. The drop location is still the origin.
    @param originPoint The geoCord defined as the origin

"""

class cartGeoConv:

    def alignToOrgin(pointObs: point, dropGeoCord: geoCord):
        # Naming convention (dimension)(location/origin)(R: radians, D: Degrees)
        #Cartesian of where to drop from
        x = 0-pointObs.getX()
        y = 0-pointObs.getY()
        alt = pointObs.getZ()
        R = 6378137 #equatorial raidus at earth

        #Geographical of where to go expressed in radians
        latOR = math.radians(dropGeoCord.getLat())
        lonOR = math.radians(dropGeoCord.getLon())

        #Finding where to Drop From in radians
        latLR = ((y/R) + latOR)
        lonLR = x/(2*R*math.asin(math.cos(latOR)))
        lonLR = math.asin(lonLR) + (lonOR/2)
        lonLR = lonLR*2

        #Converting back from radians to degrees
        latLD = math.degrees(latLR)
        lonLD = math.degrees(lonLR)
        output = geoCord(latLD, lonLD, alt)
        return output
