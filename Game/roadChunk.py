import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2

class RoadChunk(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 10):
        super().__init__(main, transform, zOrder)
        #-CONSTRUCTOR-
        
        #Physics Parameters
            #self.physics.scale = 0
            #self.physics.simulate = True
            #self.physics.minVel = Vec2(0, 0)
            #self.physics.colliderState = ColliderState.Block
        
        
    def update(self):
        #put your object logic here
        pass