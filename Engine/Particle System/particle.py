import pygame
from pygame.math import Vector2
from Engine.transform import Transform

class Particle:
    def __init__(self, transform: Transform, initVelocity: Vector2, lifetime, surface: pygame.Surface, deltaTime):
        self.transform = transform
        self.velocity = initVelocity
        self.lifetime = lifetime
        self.surface = surface
        self.deltatime = deltaTime

    def simulate(self):
        self.velocity.y = min(10, self.velocity.y + 0.1)
        self.transform.pos.y += self.velocity.y * self.deltatime
        self.transform.pos.x += self.velocity.x * self.deltatime