import pygame
from pygame.math import Vector2
from Engine.transform import Transform

class Particle:
    def __init__(self, transform: Transform, initVelocity: Vector2, lifetime, surface: pygame.Surface, deltaTime, owner):
        self.transform = transform
        self.velocity = initVelocity
        self.lifetime = lifetime
        self.surface = pygame.transform.scale(surface, self.transform.scale)
        self.deltatime = deltaTime
        self.owner = owner
        self.prevTime = pygame.time.get_ticks()
        
        self.curTime = pygame.time.get_ticks()

    def simulate(self):
        self.curTime = pygame.time.get_ticks()
        if self.curTime - self.prevTime >= self.lifetime:
            self.owner.particles.remove(self)
        else:
            self.transform.pos.y += self.velocity.y * self.deltatime
            self.transform.pos.x += self.velocity.x * self.deltatime