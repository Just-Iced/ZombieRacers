import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
import pygame

class RoadSide(GameObject):
        def __init__(self, main, transform : Transform, zOrder = 12, path = 'roads/straight/side'):
            super().__init__(main, path, transform, zOrder)
            self.physics.colliderState = ColliderState.Block
            
        def update(self):
            pass

class Road(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 0, path = 'roads/straight/road'):
        super().__init__(main, path, transform, zOrder)
        #-CONSTRUCTOR-
        #Physics Parameters
        self.physics.colliderState = ColliderState.Blank
        
        RoadSide(self.main, Transform(Vec2(self.transform.pos.x-55, self.transform.pos.y), 0, Vec2(12, 144)),zOrder+12)
        RoadSide(self.main, Transform(Vec2(self.transform.pos.x+55, self.transform.pos.y), 180, Vec2(12, 144)),zOrder+12)        
    def update(self):
        #self.transform.rot += 0.5
        pass

