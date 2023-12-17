import pygame, math, sys
from Engine.event import Event
from Engine.gameObject import GameObject
from Engine.transform import Transform
from pygame.math import Vector2 as Vec2
import random

#Delay Object that calculates whether or not a certain amount of time has passed and then executes an inputed event when that time has passed
class DelayEvent(GameObject):
    def __init__(self, main, TimeInMS, event, start = False):
        super().__init__(main, '', Transform(Vec2(0,0), 0, Vec2(0,0)), 0)
        self.duration = TimeInMS
        
        self.prevTime = pygame.time.get_ticks()
        
        self.curTime = pygame.time.get_ticks()
        
        self.finished = False
        
        self.Event = Event()
        
        self.Event += event
        self.start = start
        
        if self.start == True:
            
            self.Event()            
        
        
    def update(self):
        self.curTime = pygame.time.get_ticks()
        
        
        if self.curTime -  self.prevTime >= self.duration:
            self.finished = True
            if self.start == False:
                self.Event()
            self.Destroy()
            del self