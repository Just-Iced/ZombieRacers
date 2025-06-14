import sys, os
sys.path.append(os.getcwd())
import pygame

from Engine.transform import Transform
from Engine.gameObject import GameObject

class Widget(GameObject):
    def __init__(self, main, transform: Transform, zOrder: int):
        super().__init__(main, transform, zOrder)
        self.main = main
        self.boundingBox = pygame.Rect((transform.pos.x - (transform.scale.x/2))*8, (transform.pos.y - (transform.scale.y/2))*8, transform.scale.x*8, transform.scale.y*8)
        self.surface = pygame.Surface((1280, 720), pygame.SRCALPHA)#.convert_alpha()
        self.hovered = False
        self.visible = True

    def OnHovered(self):
        pass

    def OnUnHovered(self):
        pass

    def OnClicked(self):
        pass

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
    
        self.surface.fill((0,0,0,0))
        self.update()
        

    def update(self):
        pass
    
    def render(self):
        pass