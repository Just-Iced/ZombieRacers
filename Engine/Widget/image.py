from Engine.Widget.widget import Widget
from Engine.transform import Transform
import pygame
from pygame.math import Vector2
import sys, os

class Image(Widget):
    def __init__(self, main, transform: Transform, zOrder: int, path: str):
        super().__init__(main, transform, zOrder)
        self.sprite = pygame.image.load(f"{os.getcwd()}\\Game\\{path}").convert_alpha()
        self.renderOffset = Vector2(self.sprite.get_width()//2, self.sprite.get_height()//2)

    def render(self):
        self.surface.fill((0,0,0,0))
        if self.visible:
            p = self.transform.pos - self.renderOffset
            # Original: self.surface.blit(self.image, p)
            self.surface.blit(pygame.transform.scale_by(self.sprite, 8), (p.x*8, p.y*8))