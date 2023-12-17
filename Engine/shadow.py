import pygame
from Engine.gameObject import GameObject
class Shadow:
    def __init__(self, owner: GameObject):
        self.flatIMG = owner.sprites[0].copy()
        for image in owner.sprites:
            self.flatIMG.blit(image, (0,0))
        self.shadow = pygame.mask.from_surface(self.flatIMG).to_surface(setcolor=(0,0,0,100), unsetcolor=(0,0,0,0))