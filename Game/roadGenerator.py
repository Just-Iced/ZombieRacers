import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
from roadDirection import RoadDirection
from roadPiece import RoadPiece
from roadPieces.roadStraight import RoadStraight
import random
import pygame


class RoadGenerator(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 10):
        super().__init__(main, transform, zOrder)
        self.roadPieces = RoadPiece.__subclasses__()
        self.spawnPos = Vec2(0,0)
        self.previousRoad = None
        self.roads = []
        #-CONSTRUCTOR-
    
    def start(self):
        road = self.main.Instantiate(RoadStraight(self.main, Transform(self.spawnPos, 0, Vec2(85,144))))
        self.roads.append(road)
        self.previousRoad = road
        for i in range(5):
            self.spawnNextChunk()
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t]:
            self.spawnNextChunk()


    def pickNextChunk(self) -> RoadPiece:
        exitDirection = None

        match self.previousRoad.exitDirecton:
            case RoadDirection.North:
                exitDirection = RoadDirection.South
                self.spawnPos -= Vec2(0, self.previousRoad.chunkSize.y)
            case RoadDirection.East:
                exitDirection = RoadDirection.West
                self.spawnPos += Vec2(self.previousRoad.chunkSize.x, 0)
            case RoadDirection.South:
                exitDirection = RoadDirection.North
                self.spawnPos += Vec2(0, self.previousRoad.chunkSize.y)
            case RoadDirection.West:
                exitDirection = RoadDirection.East
                self.spawnPos -= Vec2(self.previousRoad.chunkSize.x, 0)
            case None:
                return None
        possibleRoads = []
        print(self.roadPieces)
        for road in self.roadPieces:
            print(road.entryDirection)
            if road.entryDirection == exitDirection:
                possibleRoads.append(road)
        chunk = random.choice(possibleRoads)
        print(chunk)
        return chunk
    def spawnNextChunk(self):
        if len(self.roads) >=7:
            self.roads[0].Destroy()
        nextChunk = self.pickNextChunk()
        chunkToSpawn = self.main.Instantiate(nextChunk(self.main, Transform(self.spawnPos, 0, Vec2(85,16))))
        self.previousRoad = chunkToSpawn
        self.roads.append(chunkToSpawn)
