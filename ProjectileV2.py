#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:32:56 2019

@author: srikarganti
"""

import math
import numpy as np

class ProjectileV2:

    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x)."""

    # def __init__(self, originLat, originLon, xVelocity, zVelocity, xPosition, yPosition, zPosition, projectileMass):
    #     """Create a projectile with given launch angle, initial
    #     velocity and height."""
    #     self.originLat = originLat
    #     self.originLon = originLon
    #     self.position = (xPosition, yPosition, zPosition)
    #     self.velocity = (xVelocity, 0 , zVelocity)
    #     self.mass = projectileMass
    #     self.gravField = 9.8
    #     self.earthRadius = 6356.752 * 1000 #in METERS

    def __init__(self, originLat, originLon, xVelocity, zVelocity, lat, lon, altitude, projectileMass):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        self.originLat = originLat
        self.originLon = originLon
        self.convergence = math.cos(self.originLat * (math.pi / 180.0))
        self.earthRadius = 6371.000 * 1000 #in METERS
        points = self.latLongToXYZ(lat, lon)
        self.position = [points[0], points[1], altitude]
        self.velocity = [xVelocity, 0 , zVelocity]
        
        self.mass = projectileMass
        self.gravField = 9.8
        
        self.air_density = 1.225
        self.drag_coeff = 5.0
        self.wind_velocity = [-0.25,0,0]
        self.projectileRadius = 1;
        self.surfaceArea = math.pi * self.projectileRadius**2


    def getToGround(self):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        time = 0
        dt = 0.0001
        pos = list(self.position)
        vel = list(self.velocity)
        while (pos[1] >= 0):
            #Calculate forces
            gravForce = (0, -self.mass * self.gravField, 0)
           # map(operator.sub, vel, self.wind_velocity);
            #rvhat = (vel - self.wind_velocity) / math.abs(vel - self.wind_velocity) # Velocity of projectile relative to wind.
            #dragForce = 0.5 * self.air_density* self.drag_coeff*self.surfaceArea* math.abs(vel-self.wind_velocity)**2*(-rvhat)
        
            force = gravForce #+ dragForce

            #Update velocity
            vel[0] += force[0] * dt/self.mass
            vel[1] += force[1] * dt/self.mass
            vel[2] += force[2] * dt/self.mass

            #Update position
            pos[0] += vel[0] * dt
            pos[1] += vel[1] * dt
            pos[2] += vel[2] * dt

            #Update time
            time = time + dt

        return pos

    def groundToAirHelper(self, targetPos):
        landPos = self.getToGround()
        originalPos = list(self.position)

        vectorX = landPos[0] - originalPos[0]
        vectorY = landPos[1] - originalPos[1]
        vectorZ = landPos[2] - originalPos[2]

        vector = [vectorX, vectorY, vectorZ]

        return [x1 - x2 for (x1, x2) in zip(targetPos, vector)]

    def groundToAir(self, targetLat, targetLon):
        newXYZPos = self.groundToAirHelper(self.latLongToXYZ(targetLat, targetLon))
        #print(newXYZPos)
        coordinates = self.xyzToLatLong(newXYZPos[1], newXYZPos[0])
        return coordinates

    def xyzToLatLong(self, x, y):
        #lat = y / self.earthRadius + self.originLat
        #lon = math.asin(math.sin(x / self.earthRadius / 2) / math.cos(lat)) * 2 + self.originLon
        lat = (x / 111120.0) + self.originLat
        lon = ((y / (self.convergence * 111120.0)) + self.originLon)
        return [lat, lon]

    def latLongToXYZ(self, lat, lon):
        #x = 2 * self.earthRadius * math.asin(math.cos(lat) * math.sin((lon - self.originLon) / 2))
        #z = self.earthRadius * (lat - self.originLat)
        x = (lon - self.originLon) * self.convergence * 111120
        z = (lat - self.originLat) * 111120
        return [x, z]
        