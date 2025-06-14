from dataclasses import dataclass
from pygame.math import Vector2 as Vec2

@dataclass
class SystemStructure:
    speed: int = 1
    spawnRate: int = 10
    sprite: str = ''
    lifetime: int = 2
    systemLifetime: int = 2
    velocity: Vec2 = (0,0)
    scale: Vec2 = (1,1)
    randomSpread: bool = True
    randomVertical: bool = False