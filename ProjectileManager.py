#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:26:46 2019

@author: srikarganti
"""
from Projectile import Projectile

#creating new projectile object
#xVelocity, zVelocity, xPosition, yPosition, zPosition, projectileMass
proj = Projectile(7, 0, 0, 10, 0, 1)
#target point
target = [20,0,0]

print(proj.groundToAir(target))