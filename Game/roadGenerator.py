import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
from roadDirection import RoadDirection
from roadPiece import RoadPiece
import random
import pygame




class RoadGenerator(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 10):
        super().__init__(main, transform, zOrder)
        self.roadPieces = RoadPiece.__subclasses__()
        self.spawnPos = Vec2(0,0)
        print(self.roadPieces)
        #-CONSTRUCTOR-
        
        
    def pickNextChunk(self, currentRoad):
        entryDirection = None

        match currentRoad.exitDirecton:
            case RoadDirection.North:
                entryDirection = RoadDirection.South
                self.spawnPos -= Vec2(0, currentRoad.chunkSize.y)
            case RoadDirection.East:
                entryDirection = RoadDirection.West
                self.spawnPos += Vec2(currentRoad.chunkSize.x, 0)
            case RoadDirection.South:
                entryDirection = RoadDirection.North
                self.spawnPos += Vec2(0, currentRoad.chunkSize.y)
            case RoadDirection.West:
                entryDirection = RoadDirection.East
                self.spawnPos -= Vec2(currentRoad.chunkSize.x, 0)
            case None:
                return None
        possibleRoads = []
        for road in self.roadPieces:
            if road.entryDirection == entryDirection:
                possibleRoads.append(road)
        chunk = random.choice(possibleRoads)
        print(chunk)
        return chunk
        
