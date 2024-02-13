import sys, os
sys.path.append(os.getcwd())

from Engine.spriteStack import SpriteStack
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
from Engine.ParticleSystem.system import System
from Engine.gameObject import GameObject
import pygame
import time

class Shop(SpriteStack):
    def __init__(self, main, transform : Transform, zOrder = 10):
        super().__init__(main, transform, zOrder)
        #-CONSTRUCTOR-
        self.saveable = True
        #Physics Parameters
        self.physics.scale = 0
        self.physics.simulate = True
        self.physics.minVel = Vec2(0, 0)
        self.physics.colliderState = ColliderState.Overlap

        self.physics.AddSubscribersForCollisionEvent(self.collide)
    def update(self):
        #put your object logic here
        pass
    def collide(self, obj):
        if obj != self.main.player: return
        self.main.shopWidget.owner = self
        obj.showShop()

    def kill(self):
        self.main.shopWidget.setVisible(False)
        self.particles = self.main.Instantiate(System(self.main, path='ShopBreakSystem.json',transform=self.transform, zOrder=9))
        self.Destroy()

    