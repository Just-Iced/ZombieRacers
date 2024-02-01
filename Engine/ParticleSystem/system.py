import sys, os
sys.path.append(os.getcwd())

from Engine.transform import Transform
from Engine.gameObject import GameObject
from Engine.ParticleSystem.systemstucture import SystemStructure
from Engine.ParticleSystem.particle import Particle
import Engine.configRead as ConfigRead
import random
from pygame.math import Vector2 as Vec2
from Engine.functions import DelayEvent
from Engine.physicsObject import PhysicsObject
from Engine.physicsObject import ColliderState
import pygame
import math
from json import load



class System(GameObject):
    def __init__(self, main, path, transform : Transform, zOrder: int):
        self.transform = transform
        self.zOrder = zOrder
        self.main = main
        self.physics = PhysicsObject(self, False, 0)
        self.physics.colliderState = ColliderState.Blank
        self.spread = 1
        self.particles = []


        file = load(open(os.getcwd()+'\\Game\\ParticleSystems\\'+path))
        self.path = file.get('sprite')

        self.params = SystemStructure(file.get('speed'), 
                                      file.get('spawnRate'), 
                                      pygame.image.load(os.getcwd()+'\\Game\\'+self.path).convert_alpha(), 
                                      file.get('lifetime'),
                                      file.get('systemlifetime'), 
                                      Vec2(file.get('velocity')[0], file.get('velocity')[1]), 
                                      Vec2(file.get('scale')[0], file.get('scale')[1]),
                                      file.get('randomSpread'), 
                                      file.get('randomVertical'))
        

        self.prevTime = pygame.time.get_ticks()
        
        self.curTime = pygame.time.get_ticks()

        self.initvel = Vec2(file.get('velocity')[0], file.get('velocity')[1])

    def update(self):
        self.curTime = pygame.time.get_ticks()
        
        if self.curTime - self.prevTime >= self.params.systemLifetime*1000 and self.params.systemLifetime != 0:
            if self.particles == []:
                self.Destroy()
        else:
            for i in range(self.params.spawnRate):
                self.spawnParticle()

        for particle in self.particles:
            particle.simulate()
    
    def spawnParticle(self):
        scale = random.randint(round(self.params.scale[0]), round(self.params.scale[1]))

        vel = self.checkVec()
        particle = Particle(Transform(Vec2(self.transform.pos.x, self.transform.pos.y), self.transform.rot, Vec2(scale, scale)),
                                       vel,
                                        self.params.lifetime, self.params.sprite, self.main.dt, self.params.speed, self)
        
        
        self.particles.append(particle)
        
    def checkVec(self):
        if self.params.randomSpread == True:
            x = random.uniform(-self.params.velocity.x, self.params.velocity.x)
        else:
            x = self.params.velocity.x
            
        if self.params.randomVertical == True:
            y = random.uniform(-self.params.velocity.y, self.params.velocity.y)
        else:
            y = self.params.velocity.y
            
        return Vec2(x, y)