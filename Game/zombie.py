import sys, os
sys.path.append(os.getcwd())

from Engine.spriteStack import SpriteStack
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
from car import Car
import pygame

from Engine.shadow import Shadow
from Engine.ParticleSystem.system import System

class Zombie(SpriteStack):
    def __init__(self, main, transform : Transform, zOrder = 12, path = 'zombie'):
        super().__init__(main, path, transform, zOrder, cache=45)
        #-CONSTRUCTOR-
        self.shadow = Shadow(self)        
        #Physics Parameters
        self.physics.scale = 0
        self.physics.simulate = True
            #self.physics.minVel = Vec2(0, 0)
        self.physics.colliderState = ColliderState.Overlap
        self.physics.AddSubscribersForCollisionEvent(self.collide)
        
        
    def update(self):
        #put your object logic here
        pass
    def collide(self, object):
        if isinstance(object, Car):
            System(self.main,'BloodSystem.json',self.transform,self.zOrder)
            self.Destroy()
            object.coins += 1
            #print(object.coins)