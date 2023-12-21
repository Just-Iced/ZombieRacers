from Engine.Widget.widget import Widget
from Engine.transform import Transform
import pygame
from pygame.math import Vector2
from Engine.event import Event
import sys, os

class Button(Widget):
    def __init__(self, main, path, transform: Transform, zOrder=1):
        super().__init__(main, transform, zOrder)
        self.image = pygame.image.load(os.getcwd()+'/Game/UI/'+path).convert_alpha()
        self.renderOffset = Vector2(self.image.get_width(), self.image.get_height()) - Vector2(self.surface.get_width(), self.surface.get_height())
        
        self.clickEvent = Event()
        self.hoverEvent = Event()
        self.unHoverEvent = Event()
        
    def render(self):
        self.surface.fill((0,0,0))
        self.surface.blit(self.image, self.renderOffset)
        
    def OnClicked(self):
        self.clickEvent()
        
    def OnHovered(self):
        pygame.transform.scale(self.surface, (self.surface.get_width()*1.1, self.surface.get_height()*1.1))
        self.hoverEvent()
        
    def OnUnHovered(self):
        pygame.transform.scale(self.surface, (self.surface.get_width()*0.9, self.surface.get_height()*0.9))
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