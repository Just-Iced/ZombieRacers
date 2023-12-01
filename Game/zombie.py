import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
import pygame

class Zombie(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 12, path = 'zombie'):
        super().__init__(main, path, transform, zOrder)
        #-CONSTRUCTOR-
        
        #Physics Parameters
        self.physics.scale = 0
        self.physics.simulate = True
            #self.physics.minVel = Vec2(0, 0)
        self.physics.colliderState = ColliderState.Overlap
        self.physics.AddSubscribersForCollisionEvent(self.collide)
        
        
    def update(self):
        #put your object logic here
        pass
    def collide(self):
        self.main.objects.remove(self)
        self.main.colliders.remove(self.physics)