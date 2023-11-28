import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
import pygame
import math

class Car(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 1, path = 'C:/Users/Owner/Documents/GitHub/ZombieRacers/Game/car'):
        super().__init__(main, path, transform, zOrder)
        #-CONSTRUCTOR-
        
        #Physics Parameters
        self.physics.scale = 0
        self.physics.simulate = True
        self.physics.minVelocity = Vec2(0, 0)
        self.physics.colliderState = ColliderState.Block
        self.move = 0
        
        
    def update(self):
        #self.physics.setVelocity(Vec2(0, 0))
        

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
           self.transform.rot += 0.5
        elif keys[pygame.K_d]:
           self.transform.rot -= 0.5           
        if keys[pygame.K_w]:
            if self.move != -0.5:
                self.move -= 0.002
        elif keys[pygame.K_s]:
            if self.move != 0.5:
                self.move += 0.002
            
        self.physics.setVelocity(Vec2(-self.move * math.cos(math.radians(self.transform.rot + 90)), self.move * math.sin(math.radians(self.transform.rot + 90))))
                
        self.main.cam.pos = self.transform.pos
        #self.main.cam.rot = self.transform.rot
                
        
            