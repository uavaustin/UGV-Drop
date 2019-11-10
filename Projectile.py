from copy import deepcopy
class Projectile:

    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x)."""

    def __init__(self, xVelocity, zVelocity, xPosition, yPosition, zPosition, projectileMass):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        self.position = (xPosition, yPosition, zPosition)
        self.velocity = (xVelocity, 0 , zVelocity)
        self.mass = projectileMass
        self.gravField = 9.8
        
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
            
            force = gravForce
            
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
    
    def groundToAir(self, targetPos):
        landPos = self.getToGround()
        originalPos = list(self.position)
        
        vectorX = landPos[0] - originalPos[0]
        vectorY = landPos[1] - originalPos[1]
        vectorZ = landPos[2] - originalPos[2]
        
        vector = [vectorX, vectorY, vectorZ]
        
        return [x1 - x2 for (x1, x2) in zip(targetPos, vector)]
        
        
        
        

    @staticmethod
    def getY(self):
        "Returns the y position (height) of this projectile."
        return self.ypos

    def getX(self):
        "Returns the x position (distance) of this projectile."
        return self.xpos
    
    def getZ(self):
        "Returns the z position (distance) of this projectile."
        return self.zpos