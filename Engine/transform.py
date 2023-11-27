from dataclasses import dataclass
from pygame.math import Vector2

@dataclass
class Transform:
    pos: Vector2 = (0,0)
    rot: int = 0