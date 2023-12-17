from pygame.math import Vector2 as Vec2
from Engine.transform import Transform
from Engine.physicsObject import PhysicsObject
import pygame
import os

import sys, os


class GameObject:
    def __init__(self, main, transform : Transform, zOrder = int):
        self.transform = transform
        self.zOrder = zOrder
        self.main = main
        self.physics = PhysicsObject(self, False, 1)
        self.spread = 1
        self.main.objects.append(self)
    
    def tick(self):
        self.update()
    
    def update(self):
        pass