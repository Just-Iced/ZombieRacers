import sys, os
sys.path.append(os.getcwd())
import pygame

from Engine.transform import Transform
from Engine.gameObject import GameObject

class Widget(GameObject):
    def __init__(self, main, transform: Transform):
        super().__init__(main, transform, 0)
        self.main = main
        self.boundingBox = pygame.Rect((transform.pos.x - (transform.scale.x/2))*8, (transform.pos.y - (transform.scale.y/2))*8, transform.scale.x*8, transform.scale.y*8)
        self.surface = pygame.Surface((160, 90), pygame.SRCALPHA)#.convert_alpha()
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
    
    def render(self):
        pass