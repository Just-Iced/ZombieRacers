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
        super().__init__(main, transform, zOrder)
        #-CONSTRUCTOR-
        
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
        self.coins = 0
        self.particles = System(main, path='DirtSystem.json',transform=self.transform, zOrder=9)
        self.main.cam.rot = self.transform.rot
        #self.savefile = "C:/Users/585622/Documents/GitHub/ZombieRacers/Game/savefile"
        
        #with open(self.savefile, "r") as savefile:
            #data = pickle.load(open(self.savefile))
            #print(f"Save Data: \n{data}")
        
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
                player_data = {"coins" : self.coins}
                with open(self.savefile, "rw") as f:
                    data = pickle.load(f)
                    data["player"] = player_data
                    pickle.dump(data, f)
                    

        
    def resetVel(self):
        #self.move = 0
        self.move = self.move/2
        
    def kill(self):
        self.maxSpeed = 0
        self.acceleration = 0
        self.move = 0
        self.physics.setVelocity(Vec2(0,0))

                
        
            