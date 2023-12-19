import sys, os
sys.path.append(os.getcwd())
import pygame

from Engine.transform import Transform
from Engine.gameObject import GameObject

class Widget(GameObject):
    def __init__(self, main, transform : Transform, zOrder = int):
        super().__init__(main, transform, zOrder)
        self.boundingBox = pygame.Rect(transform.pos, transform.scale)
        self.surface = pygame.Surface((160, 90)).convert_alpha()
        self.hovered = False

    def OnHovered(self):
        print("Hovered")

    def OnUnHovered(self):
        print("Un-Hovered")

    def OnClicked(self):
        print("Clicked")

    def tick(self):
        mouse = pygame.mouse.get_pos()
        
        #hovered detection
        if self.boundingBox.collidepoint(mouse):
            if self.hovered == False:
                self.OnHovered()
            self.hovered = True
        else:
            if self.hovered == True:
                self.OnUnHovered()
            self.hovered = False
        for event in self.main.events:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == True and self.hovered == True:
                self.OnClicked()
    

        self.update()

    def update(self):
        pass