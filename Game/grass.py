import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
import pygame

from Engine.shadow import Shadow

class Grass(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 10, path = 'grass'):
        super().__init__(main, path, transform, zOrder)
        #-CONSTRUCTOR-
        self.shadow = Shadow(radius=12)    
        #Physics Parameters
        self.physics.colliderState = ColliderState.Block