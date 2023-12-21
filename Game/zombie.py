
import sys, os

sys.path.append(os.getcwd())

from Engine.spriteStack import SpriteStack
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
from car import Car
from coin import Coin
import pygame
import random
import math
import time

from Engine.shadow import Shadow
from Engine.ParticleSystem.system import System

class Zombie(SpriteStack):
    def __init__(self, main, transform : Transform, zOrder = 10):
        super().__init__(main, transform, zOrder)
        #-CONSTRUCTOR-
        self.shadow = Shadow(self)        
        #Physics Parameters
        self.physics.scale = 0
        self.physics.simulate = True
            #self.physics.minVel = Vec2(0, 0)
        self.physics.colliderState = ColliderState.Overlap
        self.physics.AddSubscribersForCollisionEvent(self.collide)
        self.startTime = round(time.time())
        self.ranOffset = 0
        
    def update(self):
        if round(time.time()) - self.startTime >= 25:
            self.Destroy()
        if random.randint(0,100) == 69:
            self.ranOffset = random.uniform(-15,15)
        #put your object logic here
        speed = 0.5
        relativePos: Vec2 = self.main.player.transform.pos - self.transform.pos
        if relativePos.distance_to(Vec2(0,0)) > 100:
            speed = 5

        angle = (180/math.pi) * -math.atan2(relativePos.y,relativePos.x) + self.ranOffset
        self.transform.rot = angle + 90
        self.physics.setVelocity(Vec2(speed,0).rotate(-angle))
    def collide(self, object):
        if isinstance(object, Car):
            System(self.main,'BloodSystem.json',self.transform,self.zOrder)
            for i in range(random.randint(1,5)):
                Coin(self.main, Transform(self.transform.pos + Vec2(random.uniform(-1,1),random.uniform(-1,1)), scale=Vec2(1,1)), self.zOrder)
            self.Destroy()
            #print(object.coins)