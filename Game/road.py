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
import random
import pygame
import threading

class RoadSide(SpriteStack):
    def __init__(self, main, transform : Transform, zOrder = 20):
        super().__init__(main, transform, zOrder)
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
            self.Destroy()
            Road(self.main, Transform(Vec2(0,72) + self.transform.pos, 0, Vec2(85,16)))

class RoadDestroy(GameObject):
    def __init__(self, main, road: "Road", transform: Transform, zOrder=0, RoadDestroyer=True):
        super().__init__(main, transform, zOrder)
        self.physics.colliderState = ColliderState.Overlap
        self.physics.simulate = True
        self.physics.scale = 0
        self.physics.AddSubscribersForCollisionEvent(self.try_Destroy_road)
        self.road = road
        self.should_RoadDestroy = RoadDestroyer
    def try_Destroy_road(self, object):
        if not isinstance(object, Car):
            return
        if self.should_RoadDestroy:
            if not self.road.exists:
                return
            for child in self.road.children:
                x = threading.Thread(target=child.Destroy)
                x.start()
                x.join()
            self.road.Destroy()
            self.road.exists = False
        else:
            self.road.replace_road()


class Road(SpriteStack):
    def __init__(self, main, transform : Transform, zOrder = 0):
        super().__init__(main, transform, zOrder)
        #-CONSTRUCTOR-
        #Physics Parameters
        self.physics.colliderState = ColliderState.Blank
        self.children = []
        x = threading.Thread(target=self.spawn)
        x.start()
        x.join()
        for i in range(random.randint(0,5)):
            x = threading.Thread(target=self.spawn_zombie)
            x.start()
            x.join()
    def spawn(self):
        self.children.append(RoadSide(self.main, Transform(Vec2(self.transform.pos.x-55, self.transform.pos.y), 0, Vec2(12, 144))))
        self.children.append(RoadSide(self.main, Transform(Vec2(self.transform.pos.x+55, self.transform.pos.y), 180, Vec2(12, 144))))        
        RoadEnd(self.main, transform=Transform(self.transform.pos + Vec2(0, 72), scale=Vec2(85,85)))
        RoadDestroy(self.main, transform=Transform(self.transform.pos + Vec2(0, 720), scale=Vec2(85,85)),road=self)
        RoadDestroy(self.main, transform=Transform(self.transform.pos + Vec2(0, 571), scale=Vec2(85,85)),road=self,RoadDestroyer=False)
        RoadDestroy(self.main, transform=Transform(self.transform.pos - Vec2(0, 720), scale=Vec2(85,85)),road=self)
        RoadDestroy(self.main, transform=Transform(self.transform.pos - Vec2(0, 571), scale=Vec2(85,85)),road=self,RoadDestroyer=False)
        self.exists = True
    def update(self):
        #self.transform.rot += 0.5
        pass

    def spawn_zombie(self):
        pos = Vec2(random.randint(-42,42), random.randint(-72,72)) + self.transform.pos
        self.children.append(Zombie(self.main,Transform(pos,random.randint(-180,180),Vec2(3,3))))
    def spawn_child(self, child):
        child.main.objects.append(child)
        child.main.colliders.append(child.physics)
    def replace_road(self):
        if not self.exists:
            self.main.objects.append(self)
            self.main.colliders.append(self.physics)
            for child in self.children:
                x = threading.Thread(target=lambda: self.spawn_child(child))
                x.start()
                x.join()
            self.exists = True