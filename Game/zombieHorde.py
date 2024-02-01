import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.sprite import Sprite
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
import pygame

class ZombieHorde(Sprite):
    def __init__(self, main, transform : Transform, zOrder = 10,):
        super().__init__(main, transform=transform, zOrder=zOrder, path="ZombieHorde.png")
        #-CONSTRUCTOR-
        self.saveable = True
        #Physics Parameters
        self.physics.scale = 0
        self.physics.simulate = True
        self.physics.minVel = Vec2(0, 0)
        self.physics.colliderState = ColliderState.Overlap
        self.physics.setVelocity(Vec2(0,0.25))
        self.physics.AddSubscribersForCollisionEvent(self.collide)
    def collide(self, object):
        if object != self.main.player:
            return
        self.main.player.kill()
        self.Destroy()
    def update(self):
        ...
        #put your object logic here
        #self.physics.setVelocity(self.physics.velocity + Vec2(0,0.025 * self.main.dt))
