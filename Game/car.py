import sys, os
sys.path.append(os.getcwd())

from Engine.spriteStack import SpriteStack
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
import Engine.serialization as serialize
from pygame.math import Vector2 as Vec2
import pygame
import math
import pickle

from Engine.shadow import Shadow
from Engine.ParticleSystem.system import System
class Car(SpriteStack):
    def __init__(self, main, transform : Transform, zOrder = 10):
        super().__init__(main, transform, zOrder)        
        #-CONSTRUCTOR-
        self.data = {}

        self.attributes = {"Max Speed": 5, 
                      "Acceleration": 0.06, 
                      "Coin Multiplier": 1}
        
        self.shadow = Shadow(self)

        #Physics Parameters
        self.physics.scale = 0
        self.physics.simulate = True
        self.physics.minVel = Vec2(0, 0)
        self.physics.colliderState = ColliderState.Block
        self.physics.AddSubscribersForHitEvent(self.resetVel)
        self.move = 0
        self.camOffset = 5
        self.maxSpeed = 5
        self.acceleration = 0.06
        self.coins = 100
        self.coinMultiplier = 1
        self.particles = None
        self.main.cam.rot = -self.transform.rot

        self.curVel = Vec2(0,0)
        self.curMove = 0
        
        if serialize.DoesSaveDataExist("car"):
            self.data = serialize.LoadSaveData("car")
            self.load()
    
    def start(self):
        self.particles = self.main.Instantiate(System(self.main, path='DirtSystem.json',transform=self.transform, zOrder=9))
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.move != 0:
            self.transform.rot += 2 * self.main.dt# / (self.maxSpeed - self.move*2)
            #self.main.cam.rot -= 2 * self.main.dt #/ (self.maxSpeed - self.move*2)
        elif keys[pygame.K_d] and self.move != 0:
            self.transform.rot -= 2 * self.main.dt #/ (self.maxSpeed - self.move*2)
            #self.main.cam.rot += 2 * self.main.dt #/ (self.maxSpeed - self.move*2)
            #self.move += 0.01 * self.main.dt
        
        if keys[pygame.K_w]:
            if self.move >= -self.maxSpeed:
                self.move -= self.acceleration * self.main.dt
        else:
            if self.move < 0:
                self.move += self.acceleration * self.main.dt
                #self.move = max(self.move, 0)
            elif self.move > 0:
                self.move = 0
        self.particles.params.velocity = self.particles.initvel * -self.move
        self.physics.setVelocity(Vec2(-self.move * math.cos(math.radians(self.transform.rot + 90)), self.move * math.sin(math.radians(self.transform.rot + 90))))
        self.curVel = self.physics.velocity
        self.curMove = self.move

        self.main.cam.pos = self.main.cam.pos.lerp(self.transform.pos, self.maxSpeed / 10)
        self.attributes = {"Max Speed": self.maxSpeed, "Acceleration": self.acceleration, 
                            "Coin Multiplier": self.coinMultiplier}

        self.main.cam.rot = pygame.math.lerp(self.main.cam.rot, -self.transform.rot, 0.05)

        for event in self.main.events:
            if event.type == pygame.QUIT:
                self.save()
            
                    
                        
    def showShop(self):
        self.main.shopWidget.setVisible(True)

    def hideShop(self):
        self.main.shopWidget.setVisible(False)
        self.main.shopWidget.owner.kill()
                    
    def load(self):
        self.coins = self.data['Coins']
        self.transform = self.data['Pos']
        self.maxSpeed = self.data['Max Speed']
        self.acceleration = self.data['Acceleration']
        self.coinMultiplier = self.data['Coin Multiplier']

        self.attributes = {"Max Speed": self.data['Max Speed'], 
                            "Acceleration": self.data['Acceleration'], 
                            "Coin Multiplier": self.data['Coin Multiplier']}
        self.main.cam.rot = -self.transform.rot
        
    def save(self):
        self.data = {"Coins" : self.coins, "Pos" : self.transform, 
                     "Max Speed": self.maxSpeed, "Acceleration": self.acceleration, 
                     "Coin Multiplier": self.coinMultiplier}
        serialize.SaveData("car", self.data)
        
    def resetVel(self):
        #self.move = 0
        self.move = self.move/2
        
    def kill(self):
        """self.maxSpeed = 0
        self.acceleration = 0
        self.move = 0
        self.physics.setVelocity(Vec2(0,0))"""
        pass

                
        
            