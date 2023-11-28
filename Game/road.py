import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
import pygame

class Road(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 0, path = 'roads'):
        super().__init__(main, path, transform, zOrder)
        #-CONSTRUCTOR-
        #Physics Parameters
        self.physics.colliderState = None
    def update(self):
        #self.transform.rot += 0.5
        pass