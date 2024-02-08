from Engine.Widget.widget import Widget
from Engine.transform import Transform
import pygame
from pygame.math import Vector2
from Engine.event import Event
import sys, os

class Text(Widget):
    def __init__(self, main, text: str, transform: Transform, fontName: str = "Pixellari.ttf"):
        super().__init__(main, transform)
        path = f"{os.getcwd()}\\Engine\\Widget\\{fontName}"
        self.font = pygame.font.Font(path,16)
        self.text = text
        self.colour = (255,255,255)

    def update(self):
        img = self.font.render(self.text,True,self.colour)
        self.surface.blit(img,self.transform.pos.xy)