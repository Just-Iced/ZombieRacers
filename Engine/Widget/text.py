from Engine.Widget.widget import Widget
from Engine.transform import Transform
import pygame
from pygame.math import Vector2 as Vec2
from Engine.event import Event
import sys, os

class Text(Widget):
    def __init__(self, main, text: str, transform: Transform, zOrder: int, colour = pygame.color.Color(255,255,255), size=64, fontName: str = "Pixellari.ttf", ):
        super().__init__(main, transform, zOrder)

        path = f"{os.getcwd()}\\Game\\UI\\{fontName}"
        self.font = pygame.font.Font(path, size)
        self.text = text
        self.colour = colour

    def render(self):
        if self.visible:
            img = self.font.render(self.text,False,self.colour)
            self.surface.blit(img,self.transform.pos.xy)