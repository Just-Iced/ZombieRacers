import sys, os

from Engine.spriteStack import SpriteStack
from Game.car import Car
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

        self.physics.AddSubscribersForCollisionEvent(self.hit)
        self.speed = random.uniform(-2,2)
        self.player = self.main.player
        self.physics.setVelocity(Vec2(self.speed, self.speed))
        
    def update(self):
        DirVec = -(self.transform.pos - self.player.transform.pos) / 500
        
        self.physics.setVelocity(self.physics.velocity + DirVec)
        
    def hit(self,object):
        if object.__class__.__name__ == "Car":
            object.coins += 1
            print(object.coins)
            self.Destroy()
        else:
            self.speed = 0