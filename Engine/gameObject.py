from pygame.math import Vector2 as Vec2
from transform import Transform
import pygame
import os

class GameObject:
    def __init__(self, main, path, transform : Transform, zOrder = int):
        self.transform = transform
        self.zOrder = zOrder
        self.voxelPath = path
        self.sprites = [pygame.image.load(self.voxelPath+"/"+img) for img in os.listdir(self.voxelPath)]
        self.main = main