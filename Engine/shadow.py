import pygame

class Shadow:
    def __init__(self, radius):
        self.surf = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        self.shadow = pygame.draw.circle(self.surf, (0,0,0, 80), (radius, radius), radius)