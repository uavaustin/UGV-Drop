#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:26:46 2019

@author: srikarganti
"""
from Projectile import Projectile
from ProjectileV2 import ProjectileV2
from ProjectileV3 import ProjectileV3

#creating new projectile object
#xVelocity, zVelocity, xPosition, yPosition, zPosition, projectileMass
proj = Projectile(7, 0, 0, 10, 0, 1)
#target point
target = [20,0,0]

newProj = ProjectileV2(89.9981086813, 45.0000000000, 0, 0, 89.9981086813, 78.6900675260, 5, 1)

#print(proj.groundToAir(target))
print("Total conversion")
print(newProj.groundToAir(89.9981086813, 78.6900675260))

finalProj = ProjectileV3(89.9981086813, 45.0000000000, 1, 89.9981086813, 78.6900675260)
finalProj.updatePosition(0, 0, 89.9981086813, 78.6900675260, 5)

print(finalProj.groundToAir())

finalProj.updatePosition(0, 0, 89.9981086813, 78.6900675260, 5)
print(finalProj.groundToAir())