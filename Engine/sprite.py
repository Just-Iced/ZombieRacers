from Engine.gameObject import GameObject
from Engine.transform import Transform
import pygame
import os

class Sprite(GameObject):
    def __init__(self, main, path, transform: Transform, zOrder: int):
        super().__init__(main, path, transform, zOrder)

        self.sprites = [pygame.image.load(os.getcwd()+'/Game/'+path)]