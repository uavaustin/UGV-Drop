#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:32:56 2019

@author: srikarganti
"""

import math
import numpy as np

class ProjectileV3:

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

    def __init__(self, originLat, originLon, projectileMass, targetLat, targetLon):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        np.set_printoptions(precision=20)
        self.originLat = originLat
        self.originLon = originLon
        
        self.targetLat = targetLat;
        self.targetLon = targetLon;
        
        self.convergence = math.cos(self.originLat * (math.pi / 180.0))
        self.earthRadius = 6371.000 * 1000 #in METERS
        
        #self.position;
        #self.velocity;
        
        self.mass = projectileMass
        self.gravField = 9.8
        
        self.air_density = 1.225
        self.drag_coeff = 5.0
        self.wind_velocity = [-0.0001,-0.00001, -0.00001]
        self.projectileRadius = 1;
        self.surfaceArea = math.pi * self.projectileRadius**2


    def getToGround(self):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        time = 0
        dt = 0.0001
        pos = np.copy(self.position)
        vel = np.copy(self.velocity)
        while (pos[1] >= 0):
            #Calculate forces
            gravForce = np.array([0, -self.mass * self.gravField, 0])
            rvhat = np.subtract(vel, self.wind_velocity) / np.absolute(np.subtract(vel, self.wind_velocity)) # Velocity of projectile relative to wind.
            
            dragForce = 0.5 * self.air_density* self.drag_coeff*self.surfaceArea * np.absolute(np.subtract(vel, self.wind_velocity))**2*(-rvhat)
            
            force = gravForce + dragForce
            
            
            #Update Velocity
            vel = np.add(vel, force * dt/self.mass)
            
            #Update position
            pos = np.add(pos, vel * dt)
            
            #Update time
            time = time + dt

        return pos

    def groundToAirHelper(self, targetPos):
        landPos = self.getToGround()
        originalPos = self.position

        vectorX = landPos[0] - originalPos[0]
        vectorY = landPos[1] - originalPos[1]
        vectorZ = landPos[2] - originalPos[2]

        vector = np.array([vectorX, vectorY, vectorZ])
        
        
        return np.subtract(targetPos, vector)#[x1 - x2 for (x1, x2) in zip(targetPos, vector)]

    def groundToAir(self):
        targetPos = self.latLongToXYZ(self.targetLat, self.targetLon)
        targetPos.insert(1, 0)
        newXYZPos = self.groundToAirHelper(targetPos)
        #print(newXYZPos)
        coordinates = self.xyzToLatLong(newXYZPos[2], newXYZPos[0])
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
    
    def updatePosition(self, xVelocity, zVelocity, lat, lon, altitude):
        self.velocity = [xVelocity, 0 , zVelocity]
        points = self.latLongToXYZ(lat, lon)
        self.position = [points[0], altitude, points[1]]
        