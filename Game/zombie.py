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
        self.playerOffset = random.randint(75,120)
        self.initSpeed = random.uniform(0.4,0.8)
        
    def update(self):
        if round(time.time()) - self.startTime >= 25:
            self.Destroy()
        if random.randint(0,100) == 69:
            self.ranOffset = random.randint(-15,15)
        #put your object logic here
        speed = self.initSpeed
        relativePos: Vec2 = self.main.player.transform.pos - self.transform.pos
        if relativePos.distance_to(Vec2(0,0)) > self.playerOffset:
            speed *= random.uniform(2,5)

        angle = (180/math.pi) * -math.atan2(relativePos.y,relativePos.x) + self.ranOffset
        self.transform.rot = angle + 90
        self.physics.setVelocity(Vec2(speed,0).rotate(-angle))
    def collide(self, object):
        if not isinstance(object, Car):
            return
        if object.physics.velocity.length() > 1:
            System(self.main,'BloodSystem.json',self.transform,self.zOrder)
            for i in range(random.randint(0,5)):
                Coin(self.main, Transform(self.transform.pos + Vec2(random.uniform(-1,1),random.uniform(-1,1)), scale=Vec2(1,1)), self.zOrder)
            if random.randint(0,10) == 2:
                Zombie(self.main, Transform(self.transform.pos + Vec2(random.uniform(-5,5),random.uniform(-5,5)), scale=self.transform.scale), self.zOrder)
            #print(object.coins)
        else:
            if self.main.player > 0:
                self.main.player.maxSpeed -= 0.1
            else:
                self.main.player.kill()
            System(self.main,'CarDamageSystem.json',self.main.player.transform,self.zOrder)
        self.Destroy()
            