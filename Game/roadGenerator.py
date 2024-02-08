import sys, os
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
from roadDirection import RoadDirection
from roadPiece import RoadPiece
from roadPieces.roadStraight import RoadStraight
from Engine.spawnMethod import SpawnMethod
from Engine.sprite import Sprite
import Engine.serialization as serialize
import importlib
import random
import pygame


class RoadGenerator(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 10):
        super().__init__(main, transform, zOrder)
        self.roadPieces = RoadPiece.__subclasses__()
        self.roads = []
        self.saveable = True
        self.road_dict = {}
        #-CONSTRUCTOR-
    
    def start(self):
        match self.spawnMethod:
            case SpawnMethod.Spawned:
                while len(self.roads) < 6:
                    self.spawnNextChunk()
            case SpawnMethod.Loaded:
                if serialize.DoesSaveDataExist("roads"):
                    self.road_dict = serialize.LoadSaveData("roads")
                    self.load()
            
        """for road in self.roads:
            print(f"Road is at: {road.transform.pos}")
            print(f"Road has collision: {road.physics.colliderState}")"""
        
    def update(self):
        for event in self.main.events:
            if event.type == pygame.QUIT:
                self.save()

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
        if len(self.roads) >=6:
            self.roads[0].kill()
            
            self.roads[0].physics.colliderState = ColliderState.Blank
            self.roads[1].physics.colliderState = ColliderState.Blank
            self.transform.pos = self.roads[0].transform.pos
        chunkToSpawn = self.pickNextChunk()
        
        print(f"Road is at: {chunkToSpawn.transform.pos}")
        print(f"Road has collision: {chunkToSpawn.physics.colliderState}")
        self.roads.append(chunkToSpawn)

    def load(self):
        print(self.road_dict)
        for obj in self.road_dict:
            attrs = self.road_dict[obj] #attributes
            module = importlib.import_module(attrs["module name"])
            gameObject = self.main.LoadObject(getattr(module, attrs["class name"])(main = self.main, transform = attrs["transform"], zOrder=attrs["zOrder"]))
            self.roads.append(gameObject)
        print(self.roads)
        self.transform.pos = self.roads[0].transform.pos

    def save(self):
        self.road_dict = {}
        for obj in self.roads:
            this_dict = {"module name" : obj.__module__, "class name": obj.__class__.__name__, 
                                        "transform": obj.transform, "zOrder": obj.zOrder}
            self.road_dict[str(obj.uid)] = this_dict
        serialize.SaveData("roads", self.road_dict)

