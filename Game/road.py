import imp
import sys, os
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
    def new_road(self):
        print(self.physics.overlappingObject.__class__.__name__)
        if isinstance(self.physics.overlappingObject, Car):
            Road(self.main, Transform(Vec2(0,72) + self.transform.pos, 0, Vec2(85,16)))
            self.main.objects.remove(self)
            self.main.colliders.remove(self.physics)

class Road(GameObject):
    def __init__(self, main, transform : Transform, zOrder = 0, path = 'roads/straight/road'):
        super().__init__(main, path, transform, zOrder)
        #-CONSTRUCTOR-
        #Physics Parameters
        self.physics.colliderState = ColliderState.Blank
        
        RoadSide(self.main, Transform(Vec2(self.transform.pos.x-55, self.transform.pos.y), 0, Vec2(12, 144)))
        RoadSide(self.main, Transform(Vec2(self.transform.pos.x+55, self.transform.pos.y), 180, Vec2(12, 144)))        
        RoadEnd(self.main, transform=Transform(self.transform.pos + Vec2(0, 72), scale=Vec2(85,85)))

        for i in range(random.randint(0,5)):
            pos = Vec2(random.randint(0,85), random.randint(0,144)) + self.transform.pos
            Zombie(self.main,Transform(pos,0,Vec2(3,3)))
            print(f'Zombie spawned at: {pos}')

        print(f'Road spawned at: {self.transform.pos.xy}')
    def update(self):
        #self.transform.rot += 0.5
        pass
