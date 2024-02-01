from Engine.Widget.widget import Widget
from Engine.transform import Transform
import pygame
from pygame.math import Vector2
from Engine.event import Event
import sys, os

class Text(Widget):
    def __init__(self, main, text: str, transform: Transform):
        super().__init__(main, transform)
        self.font = pygame.font.get_default_font()
        self.text = text

    def update(self):
        img = self.font.render(self.text,True,...)
        #self.surface.blit(img,(x,y))