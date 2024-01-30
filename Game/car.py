import sys, os
sys.path.append(os.getcwd())

from Engine.spriteStack import SpriteStack
from Engine.transform import Transform
from Engine.physicsObject import ColliderState
from pygame.math import Vector2 as Vec2
import pygame
import math
import pickle

from Engine.shadow import Shadow
from Engine.ParticleSystem.system import System
class Car(SpriteStack):
    def __init__(self, main, transform : Transform, zOrder = 10):
        
        #-CONSTRUCTOR-
        
        self.savefile = f"{os.getcwd()}/Game/savedata/car.pickle"
        if not os.path.isfile(self.savefile):
            with open(self.savefile, "bw") as f:
                attributes = {"coins": 0, "pos": transform}
                pickle.dump(attributes, f)
        data = pickle.load(open(self.savefile, "rb"))
        print(data)   
        self.shadow = Shadow(self)
        super().__init__(main, data["pos"], zOrder)
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
        self.coins = data["coins"]
        self.particles = System(main, path='DirtSystem.json',transform=self.transform, zOrder=9)
        self.main.cam.rot = self.transform.rot
        

         
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.move != 0:
            self.transform.rot += 2 * self.main.dt# / (self.maxSpeed - self.move*2)
            self.main.cam.rot -= 2 * self.main.dt #/ (self.maxSpeed - self.move*2)
        elif keys[pygame.K_d] and self.move != 0:
            self.transform.rot -= 2 * self.main.dt #/ (self.maxSpeed - self.move*2)
            self.main.cam.rot += 2 * self.main.dt #/ (self.maxSpeed - self.move*2)
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
        

        self.main.cam.pos = self.transform.pos
        
        for event in self.main.events:
            if event.type == pygame.QUIT:
                data = {"coins" : self.coins, "pos" : self.transform}
                with open(self.savefile, "+wb") as f:
                    print(data)
                    pickle.dump(data, f)
                    

        
    def resetVel(self):
        #self.move = 0
        self.move = self.move/2
        
    def kill(self):
        self.maxSpeed = 0
        self.acceleration = 0
        self.move = 0
        self.physics.setVelocity(Vec2(0,0))

                
        
            