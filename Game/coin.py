import sys, os

from Engine.spriteStack import SpriteStack
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.sprite import Sprite
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
import pygame
import random

class Coin(Sprite):
    def __init__(self, main, transform : Transform, zOrder = 1, path = 'Coin.png'):
        super().__init__(main,path,transform,zOrder)
        #-CONSTRUCTOR-
        
        #Physics Parameters
        self.physics.scale = 0
        self.physics.simulate = True
        self.physics.colliderState = ColliderState.Overlap
        self.newPos = self.transform.pos + Vec2(random.randrange(-5,5), random.randrange(-5,5))
        self.physics.AddSubscribersForCollisionEvent(self.hit)
        self.speed = random.randrange(4,5) / 100
        
    def update(self):
        self.transform.pos += self.newPos * self.speed * self.main.dt
        self.speed -= 0.02
    def hit(self,object):
        self.newPos = self.transform.pos