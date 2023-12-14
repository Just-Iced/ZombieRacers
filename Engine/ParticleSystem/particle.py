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

    def simulate(self):
        self.curTime = pygame.time.get_ticks()
        if self.curTime - self.prevTime >= self.lifetime:
            self.owner.particles.remove(self)
        else:
            c, s = np.cos(math.radians(self.transform.rot)), np.sin(math.radians(self.transform.rot))
            j = np.matrix([[c, s], [-s, c]])
            m = np.dot(j, [self.velocity.x, self.velocity.y])
            self.velocity = Vector2(float(m.T[0]), float(m.T[1]))
            self.transform.pos.y += (self.velocity.y * self.deltatime)*self.speed
            self.transform.pos.x += (self.velocity.x * self.deltatime)*self.speed