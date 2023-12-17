from Engine.gameObject import GameObject
from Engine.transform import Transform
import pygame
import os

class SpriteStack(GameObject):
    def __init__(self, main, transform: Transform, zOrder: int, cache: int = 90):

        self.rotCache = main.preCalc.objects[str(self.__class__.__name__)][0]
        self.cache = main.preCalc.objects[str(self.__class__.__name__)][1]
        
        super().__init__(main, transform, zOrder)