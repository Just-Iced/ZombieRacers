from dataclasses import dataclass
from Engine.gameObject import GameObject
import pygame

@dataclass
class Layer:
    object: GameObject
    surface: pygame.surface.Surface
    zOrder: int
    i: int
    transform: []