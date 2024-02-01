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
import pygame
import time

class RoadSide(SpriteStack):
    def __init__(self, main, transform : Transform, zOrder = 20):
        super().__init__(main, transform, zOrder)
        self.physics.simulate = True
        self.physics.scale = 0
        self.physics.colliderState = ColliderState.Block
    def update(self):
        pass
    
class RoadEnd(GameObject):
    def __init__(self, main, transform: Transform, zOrder=0):
        super().__init__(main, transform, zOrder)
        self.physics.colliderState = ColliderState.Overlap
        self.physics.simulate = True
        self.physics.scale = 0
        self.physics.AddSubscribersForCollisionEvent(self.new_road)
    def new_road(self, object):
        if isinstance(object, Car):
            self.main.Instantiate(Road(self.main, Transform(Vec2(0,144) + self.transform.pos, 0, Vec2(85,16))))
            self.Destroy()
            del self 

class RoadDestroy(GameObject):
    def __init__(self, main, road: "Road", transform: Transform, zOrder=0):
        super().__init__(main, transform, zOrder)
        self.physics.colliderState = ColliderState.Overlap
        self.physics.simulate = True
        self.physics.scale = 0
        self.physics.AddSubscribersForCollisionEvent(self.try_destroy_road)
        self.road = road
        self.canDestroy = True
    def try_destroy_road(self, object):
        if object != self.main.player or not self.canDestroy:
            return
        self.canDestroy = False
        for child in self.road.children:
            child.Destroy()
            del child
        self.road.Destroy()
        self.Destroy()
        del self.road
        del self

class Road(SpriteStack):
    def __init__(self, main, transform : Transform, zOrder = 0):
        super().__init__(main, transform, zOrder)
        #-CONSTRUCTOR-
        self.saveable = True
        #Physics Parameters
        self.physics.colliderState = ColliderState.Blank
        self.children = []
    
    def start(self):
        self.spawn()
        if self.spawnMethod == SpawnMethod.Spawned:
            for i in range(random.randint(0,5)):
                self.spawn_zombie()
    def spawn(self):
        self.children.append(self.main.Instantiate(RoadSide(self.main, Transform(Vec2(self.transform.pos.x-55, self.transform.pos.y), 0, Vec2(12, 144)))))
        self.children.append(self.main.Instantiate(RoadSide(self.main, Transform(Vec2(self.transform.pos.x+55, self.transform.pos.y), 180, Vec2(12, 144))))) 
        self.main.Instantiate(RoadEnd(self.main, transform=Transform(self.transform.pos + Vec2(0, 72), scale=Vec2(85,85))))
        self.main.Instantiate(RoadDestroy(self.main, transform=Transform(self.transform.pos + Vec2(0, 720), scale=Vec2(85,85)),road=self))
        
    def update(self):
        #self.transform.rot += 0.5
        pass
    def spawn_zombie(self):
        pos = Vec2(random.randint(-42,42), random.randint(-72,72)) + self.transform.pos
        self.main.Instantiate(Zombie(self.main,Transform(pos,random.randint(-180,180),Vec2(3,3))))