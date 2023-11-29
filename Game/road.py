import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
import pygame

class RoadSide(GameObject):
        def __init__(self, main, transform : Transform, zOrder = 0, path = 'roads/straight/side'):
            super().__init__(main, path, transform, zOrder)
            self.physics.colliderState = ColliderState.Block
        def update(self):
            pass

class Road(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 0, path = 'roads/straight/road'):
        super().__init__(main, path, transform, zOrder)
        #-CONSTRUCTOR-
        test = RoadSide(main, Transform(Vec2(transform.pos.x + 110, transform.pos.y),transform.rot,transform.scale),zOrder + 1)
        test2 = RoadSide(main, Transform(Vec2(transform.pos.x + 10, transform.pos.y),transform.rot,transform.scale),zOrder + 1)
        #Physics Parameters
        self.physics.colliderState = None
    def update(self):
        #self.transform.rot += 0.5
        pass

