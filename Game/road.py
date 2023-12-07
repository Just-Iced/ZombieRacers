import sys, os
from telnetlib import GA
sys.path.append(os.getcwd())

from Engine.gameObject import GameObject
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
from zombie import Zombie
from car import Car
import random
import pygame

class RoadSide(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 50, path = 'roads/straight/side'):
        super().__init__(main, path, transform, zOrder)
        self.physics.colliderState = ColliderState.Block
        
    def update(self):
        pass
class RoadEnd(GameObject):
    def __init__(self, main, transform: Transform, path="", zOrder=-10):
        super().__init__(main, path, transform, zOrder)
        self.physics.colliderState = ColliderState.Overlap
        self.physics.simulate = True
        self.physics.scale = 0
        self.physics.AddSubscribersForCollisionEvent(self.new_road)
        print(self.transform.pos)
    def new_road(self, object):
        if isinstance(object, Car):
            self.Destroy()
            print(object.__class__.__name__)
            Road(self.main, Transform(Vec2(0,72) + self.transform.pos, 0, Vec2(85,16)))

class RoadDestroy(GameObject):
    def __init__(self, main, road: GameObject, transform: Transform, path="", zOrder=-10):
        super().__init__(main, path, transform, zOrder)
        self.physics.colliderState = ColliderState.Overlap
        self.physics.simulate = True
        self.physics.scale = 0
        self.physics.AddSubscribersForCollisionEvent(self.destroy_road)
        self.road = road
        print(self.transform.pos)
    def destroy_road(self, object):
        if isinstance(object, Car):
            for child in self.road.children:
                child.Destroy()
            self.road.Destroy()
            self.Destroy()


class Road(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 0, path = 'roads/straight/road'):
        super().__init__(main, path, transform, zOrder)
        #-CONSTRUCTOR-
        #Physics Parameters
        self.physics.colliderState = ColliderState.Blank
        self.children = []
        
        self.children.append(RoadSide(self.main, Transform(Vec2(self.transform.pos.x-55, self.transform.pos.y), 0, Vec2(12, 144))))
        self.children.append(RoadSide(self.main, Transform(Vec2(self.transform.pos.x+55, self.transform.pos.y), 180, Vec2(12, 144))))        
        RoadEnd(self.main, transform=Transform(self.transform.pos + Vec2(0, 72), scale=Vec2(85,85)))
        RoadDestroy(self.main, transform=Transform(self.transform.pos + Vec2(0, 720), scale=Vec2(85,85)),road=self)

        for i in range(random.randint(0,5)):
            pos = Vec2(random.randint(-42,42), random.randint(-72,72)) + self.transform.pos
            self.children.append(Zombie(self.main,Transform(pos,random.randint(-180,180),Vec2(3,3))))
        print(f'Road spawned at: {self.transform.pos.xy}')
    def update(self):
        #self.transform.rot += 0.5
        pass
