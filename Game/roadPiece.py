import sys, os
from telnetlib import GA
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.spriteStack import SpriteStack
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
from zombie import Zombie
from car import Car
from Engine.spawnMethod import SpawnMethod
import random

class RoadPiece(SpriteStack):
    entryDirection = None
    exitDirecton = None
    def __init__(self, main, transform : Transform, zOrder = 0):
        super().__init__(main, transform, zOrder)
        #-CONSTRUCTOR-
        #Physics Parameters
        self.physics.colliderState = ColliderState.Overlap
        self.children = []
        self.spawnPos = Vec2(0,0)
        self.chunkSize = Vec2(144,144)

        self.physics.scale = 0
        self.physics.simulate = True
        self.physics.AddSubscribersForCollisionEvent(self.spawnNewRoad)
        
        
    def start(self):
        if self.spawnMethod == SpawnMethod.Spawned:
            for i in range(random.randint(0,5)):
                self.spawn_zombie()

    def update(self):
        if self not in self.main.roadGenerator.roads:
            self.kill()
    def spawn_zombie(self):
        pos = Vec2(random.randint(-42,42), random.randint(-72,72)) + self.transform.pos
        self.main.Instantiate(Zombie(self.main,Transform(pos,random.randint(-180,180),Vec2(3,3))))

    def spawnNewRoad(self, obj):
        if not isinstance(obj, Car):
            return
        self.main.roadGenerator.spawnNextChunk()
    def kill(self):
        for child in self.children:
            child.Destroy()
        if self in self.main.roadGenerator.roads:
            self.main.roadGenerator.roads.remove(self)
        self.Destroy()