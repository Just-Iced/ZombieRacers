import pygame
from pygame.math import Vector2 
import math
import numpy as np
from Engine.transform import Transform

class Particle:
    def __init__(self, transform: Transform, initVelocity: Vector2, lifetime, surface: pygame.Surface, deltaTime, speed, owner):
        self.transform = transform
        self.velocity = initVelocity
        self.lifetime = lifetime
        self.surface = pygame.transform.scale(surface, self.transform.scale)
        self.deltatime = deltaTime
        self.owner = owner
        self.speed = speed
        self.prevTime = pygame.time.get_ticks()
        
        self.curTime = pygame.time.get_ticks()
        vel = Vector2(-(self.velocity.x * math.cos(math.radians(self.transform.rot- 180))) - self.velocity.y * math.sin(math.radians(self.transform.rot- 180)),
                      self.velocity.x * math.sin(math.radians(self.transform.rot - 180)) - self.velocity.y * math.cos(math.radians(self.transform.rot - 180)))
        self.velocity = vel

    def simulate(self):
        self.curTime = pygame.time.get_ticks()
        if self.curTime - self.prevTime >= self.lifetime:
            self.owner.particles.remove(self)
        else:
            self.transform.pos.y += (self.velocity.y * self.deltatime)*self.speed
            self.transform.pos.x += (self.velocity.x * self.deltatime)*self.speed