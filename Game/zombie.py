import sys, os

sys.path.append(os.getcwd())

from Engine.spriteStack import SpriteStack
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from Engine.sound import Sound
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
        #self.saveable = True
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
        self.playing = False
        self.groans = os.listdir(f"{os.getcwd()}\\Game\\sounds\\Zombie\\Groans")
        self.sound = None
        self.damage = 0.1

    def update(self):
        if round(time.time()) - self.startTime >= 25:
            self.Destroy()
        if random.randint(0,100) == 69:
            self.ranOffset = random.randint(-15,15)
            if random.randint(0,10) == 5:
                self.play_groan()
        #put your object logic here
        speed = self.initSpeed
        relativePos: Vec2 = self.main.player.transform.pos - self.transform.pos
        distance_to = relativePos.distance_to(Vec2(0,0))
        if distance_to > self.playerOffset * 5:
            self.Destroy()
            return
        elif distance_to > self.playerOffset:
            speed *= random.uniform(2,4)

        angle = (180/math.pi) * -math.atan2(relativePos.y,relativePos.x) + self.ranOffset
        self.transform.rot = angle + 90
        self.physics.setVelocity(Vec2(speed,0).rotate(-angle))
        
    def collide(self, object):
        if not isinstance(object, Car):
            return
        if object.physics.velocity.length() > 1:
            self.main.Instantiate(System(self.main,'BloodSystem.json',self.transform,self.zOrder))
            for i in range(random.randint(0,5)):
                self.main.Instantiate(Coin(self.main, Transform(self.transform.pos + Vec2(random.uniform(-1,1),random.uniform(-1,1)), scale=Vec2(1,1)), self.zOrder))
        else:
            if self.main.player.maxSpeed > 0:
                self.main.player.maxSpeed -= self.damage
            else:
                self.main.player.kill()
            self.main.Instantiate(System(self.main,'CarDamageSystem.json',self.main.player.transform,self.zOrder))
        if self.sound != None:
            self.sound.Destroy()
        self.Destroy()
        
    def play_groan(self):
        if self.sound != None:
            self.sound.Destroy()
        self.sound = self.main.Instantiate(Sound(self.main, self.transform, 200, f"Zombie\\Groans\\{random.choice(self.groans)}"))
        self.playing = True