import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
from roadDirection import RoadDirection
from roadPiece import RoadPiece
from roadPieces.roadStraight import RoadStraight
from Engine.sprite import Sprite
import random
import pygame


class RoadGenerator(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 10):
        super().__init__(main, transform, zOrder)
        self.roadPieces = RoadPiece.__subclasses__()
        self.roads = []
        self.saveable = True
        
        #-CONSTRUCTOR-
    
    def start(self):
        while len(self.roads) < 7:
            self.spawnNextChunk()
            
        """for road in self.roads:
            print(f"Road is at: {road.transform.pos}")
            print(f"Road has collision: {road.physics.colliderState}")"""
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t]:
            self.spawnNextChunk()


    def pickNextChunk(self) -> RoadPiece:
        exitDirection = None
        if len(self.roads) == 0:
            road = self.main.Instantiate(RoadStraight(self.main, Transform(self.transform.pos, 0, Vec2(85,144))))
            road.physics.colliderState = ColliderState.Blank
            self.roads.append(road)
        previousRoad = self.roads[-1]
        spawnPos = previousRoad.transform.pos
        match previousRoad.exitDirecton:
            case RoadDirection.North:
                exitDirection = RoadDirection.South
                spawnPos += Vec2(0, previousRoad.chunkSize.y)
            case RoadDirection.East:
                exitDirection = RoadDirection.West
                spawnPos += Vec2(previousRoad.chunkSize.x, 0)
            case RoadDirection.South:
                exitDirection = RoadDirection.North
                spawnPos -= Vec2(0, previousRoad.chunkSize.y)
            case RoadDirection.West:
                exitDirection = RoadDirection.East
                spawnPos -= Vec2(previousRoad.chunkSize.x, 0)
            case None:
                return None
        print(f"Spawn Pos is: {spawnPos}")
        
        possibleRoads = []
        for road in self.roadPieces:
            #print(road.entryDirection)
            if road.entryDirection == exitDirection:
                possibleRoads.append(road)
        chunk = random.choice(possibleRoads)

        return self.main.Instantiate(chunk(self.main, Transform(round(spawnPos), 0, Vec2(85,72))))
    
    

    def spawnNextChunk(self):
        if len(self.roads) >=7:
            self.roads[0].Destroy()
            self.roads.pop(0)
            self.roads[0].physics.colliderState = ColliderState.Blank
            self.roads[1].physics.colliderState = ColliderState.Blank
            self.transform.pos = self.roads[0].transform.pos
        chunkToSpawn = self.pickNextChunk()
        
        print(f"Road is at: {chunkToSpawn.transform.pos}")
        print(f"Road has collision: {chunkToSpawn.physics.colliderState}")
        self.roads.append(chunkToSpawn)
