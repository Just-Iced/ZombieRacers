from Engine.transform import Transform
from pygame.math import Vector2 as Vec2
from roadPiece import RoadPiece
from roadDirection import RoadDirection

class RoadStraight(RoadPiece):
    entryDirection = RoadDirection.South
    exitDirecton = RoadDirection.North
    def __init__(self, main, transform: Transform, zOrder=0):
        super().__init__(main, transform, zOrder)