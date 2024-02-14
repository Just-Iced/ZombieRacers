from Engine.Widget.widget import Widget
from Engine.transform import Transform
import pygame
from pygame.math import Vector2
from Engine.event import Event
import sys, os

class Button(Widget):
    def __init__(self, main, path, transform: Transform, zOrder: int):
        super().__init__(main, transform, zOrder)
        self.image = pygame.image.load(f"{os.getcwd()}/Game/UI/{path}").convert_alpha()
        self.renderOffset = Vector2(self.image.get_width()//2, self.image.get_height()//2)
        
        self.clickEvent = Event()
        self.hoverEvent = Event()
        self.unHoverEvent = Event()
        
    def render(self):
        self.surface.fill((0,0,0,0))
        if self.visible:
            p = self.transform.pos - self.renderOffset
            # Scale by 8 to represent the usual pixel size of the screen
            # Could remove if you wanted more precisely scaled/positioned buttons
            # Original: self.surface.blit(self.image, p)
            self.surface.blit(pygame.transform.scale_by(self.image, 8), (p.x*8, p.y*8))
        
    #TODO: Fix the hover event, seems to break things rn
    def OnClicked(self):
        self.clickEvent()
        
    def OnHovered(self):
        self.hoverEvent()
        
    def OnUnHovered(self):
        self.unHoverEvent()
    
    
    
    def AddSubscribersForClickEvent(self,objMethod):
        self.clickEvent += objMethod
    
    def RemoveSubscribersForClickEvent(self,objMethod):
        self.clickEvent -= objMethod
        
        
    def AddSubscribersForHoverEvent(self,objMethod):
        self.hoverEvent += objMethod
    
    def RemoveSubscribersForHoverEvent(self,objMethod):
        self.hoverEvent -= objMethod
        
    
    def AddSubscribersForUnHoverEvent(self,objMethod):
        self.unHoverEvent += objMethod
    
    def RemoveSubscribersForUnHoverEvent(self,objMethod):
        self.unHoverEvent -= objMethod