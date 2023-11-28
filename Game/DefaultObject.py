import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
import pygame

class DefaultObject(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 1, path = ''):
        super().__init__(main, path, transform, zOrder)
        #-CONSTRUCTOR-
        
        #Physics Parameters
            #self.physics.scale = 0
            #self.physics.simulate = True
            #self.physics.minVel = Vec2(0, 0)
            #self.physics.colliderState = ColliderState.Block
        
        
    def update(self):
        #put your object logic here
        pass