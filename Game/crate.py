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

class Crate(SpriteStack):
    def __init__(self, main, transform : Transform, zOrder = 10):
        super().__init__(main, transform, zOrder)
        #-CONSTRUCTOR-
        self.saveable = True
        #Physics Parameters
        self.physics.scale = 0
        self.physics.simulate = True
        self.physics.minVel = Vec2(0, 0)
        self.physics.colliderState = ColliderState.Block
        
        CrateOverlap(main, self, Transform(self.transform.pos, scale=Vec2(18,18)), zOrder)
    def update(self):
        #put your object logic here
        pass
    
    
        
class CrateOverlap(GameObject):
    def __init__(self, main, crate: Crate, transform: Transform, zOrder=10):
        super().__init__(main, transform, zOrder)
        self.crate = crate
        
        self.physics.scale = 0
        self.physics.simulate = True
        self.physics.minVel = Vec2(0, 0)
        self.physics.colliderState = ColliderState.Overlap
        self.physics.AddSubscribersForCollisionEvent(self.collide)
    
    def collide(self, object):
        if object != self.main.player or object.physics.velocity.length() < 2:
            return
        System(self.main, "CrateBreakSystem.json", self.transform, self.zOrder + 5)
        self.crate.Destroy()
        self.Destroy()