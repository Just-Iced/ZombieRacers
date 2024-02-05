from Engine.Widget.widget import Widget
from Engine.transform import Transform
import pygame
from pygame.math import Vector2 as Vec2
from Engine.event import Event
import sys, os

class Text(Widget):
    def __init__(self, main, text: str, transform: Transform, colour = pygame.color.Color(255,255,255)):
        super().__init__(main, transform)
        self.font = pygame.font.Font(pygame.font.get_default_font(), 240)
        self.text = text
        self.colour = colour
        self.smallScreen = pygame.Surface((320,180))

    def update(self):
        img = self.font.render(self.text,True,self.colour)
        self.smallScreen.blit(img,(0,0))
        scaled = pygame.transform.scale(self.smallScreen, (20,20)).convert_alpha()
        self.surface.blit(scaled, self.transform.pos)
        