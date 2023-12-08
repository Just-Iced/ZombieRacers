import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
import pygame
import math

from Engine.shadow import Shadow

class Car(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 10, path = 'car'):
        super().__init__(main, path, transform, zOrder)
        #-CONSTRUCTOR-
        
        self.shadow = Shadow(radius=8)
        
        #Physics Parameters
        self.physics.scale = 0
        self.physics.simulate = True
        self.physics.minVel = Vec2(0, 0)
        self.physics.colliderState = ColliderState.Block
        self.physics.AddSubscribersForHitEvent(self.resetVel)
        self.move = 0
        self.camOffset = 5
        self.maxSpeed = 10
        self.acceleration = 0.06
        self.coins = 0
        
        
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.transform.rot += 2 * self.main.dt
            self.main.cam.rot -= 2 * self.main.dt
        elif keys[pygame.K_d]:
            self.transform.rot -= 2 * self.main.dt
            self.main.cam.rot += 2 * self.main.dt
            self.move += 0.01 * self.main.dt
        
        if keys[pygame.K_w]:
            if self.move >= -self.maxSpeed:
                self.move -= self.acceleration * self.main.dt
        else:
            if self.move < 0:
                self.move += self.acceleration * self.main.dt
                #self.move = max(self.move, 0)
            elif self.move > 0:
                self.move = 0

        self.physics.setVelocity(Vec2(-self.move * math.cos(math.radians(self.transform.rot + 90)), self.move * math.sin(math.radians(self.transform.rot + 90))))

        self.main.cam.pos = self.transform.pos
        
        
    def resetVel(self):
        self.move = 0
                
        
            