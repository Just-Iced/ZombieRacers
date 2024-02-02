from pygame.math import Vector2 as Vec2
from Engine.transform import Transform
from Engine.physicsObject import PhysicsObject
from Engine.spawnMethod import SpawnMethod

import os


class GameObject:
    def __init__(self, main, transform : Transform, zOrder = int):
        self.transform = transform
        self.zOrder = zOrder
        self.main = main
        self.physics = PhysicsObject(self, False, 1)
        self.spread = 1
        self.saveable = False
        self.spawnMethod = SpawnMethod.Null
        
        from uuid import uuid4
        self.uid = uuid4().hex

    
    
    def tick(self):
        self.update()

    def fixedUpdate(self):
        pass

    def start(self):
        pass
    
    def update(self):
        pass

    def Destroy(self):
        if self in self.main.objects:
            self.main.objects.remove(self)
        
        if self.physics in self.main.colliders:
            self.main.colliders.remove(self.physics)

        del self