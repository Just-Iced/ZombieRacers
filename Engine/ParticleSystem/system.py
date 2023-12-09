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
        self.lifetime = file.get('systemlifetime')*1000

        self.params = SystemStructure(file.get('speed'), file.get('spawnRate'), pygame.image.load(os.getcwd()+'\\Game\\'+file.get('sprite')).convert_alpha(), file.get('lifetime'),
                                      Vec2(file.get('velocity')[0], file.get('velocity')[1]), 
                                      (Vec2(random.randint(file.get('scale')[0][0], file.get('scale')[1][0])), 
                                      Vec2(random.randint(file.get('scale')[0][1], file.get('scale')[1][1]))),
                                      file.get('randomSpread'), file.get('randomVertical'))
        

        self.prevTime = pygame.time.get_ticks()
        
        self.curTime = pygame.time.get_ticks()
        
        self.main.objects.append(self)


    def update(self):
        self.curTime = pygame.time.get_ticks()
        
        if self.curTime - self.prevTime >= self.lifetime:
            if self.particles == []:
                self.Destroy()
        else:
            for i in range(self.params.spawnRate):
                self.spawnParticle()

        for particle in self.particles:
            particle.simulate()

    def spawnParticle(self):
        self.particles.append(Particle(Transform(Vec2(self.transform.pos.x, self.transform.pos.y), 0, Vec2(random.uniform(self.params.scale[0].x, self.params.scale[1].x), random.uniform(self.params.scale[0].y, self.params.scale[1].y))),
                                       Vec2(random.uniform(-self.params.velocity.x, self.params.velocity.x), 
                                        random.uniform(-self.params.velocity.y, self.params.velocity.y)),
                                        self.params.lifetime, self.params.sprite, self.main.dt, self))