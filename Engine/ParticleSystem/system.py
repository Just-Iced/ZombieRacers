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

import pygame
from json import load



class System(GameObject):
    def __init__(self, main, path, transform: Transform, zOrder=0):
        self.transform = transform
        self.zOrder = zOrder
        self.main = main
        self.spread = 1
        self.particles = []

        file = load(open(path))
        sys.path.append(str("Game/ParticleSystems"))


        self.params = SystemStructure(file.get('speed'), file.get('spawnRate'), pygame.image.load(file.get('sprite')).convert_alpha(), file.get('lifetime'),
                                      Vec2(file.get('velocity')[0], file.get('velocity')[1]), 
                                      (Vec2(random.randint(file.get('scale')[0][0], file.get('scale')[1][0])), 
                                      Vec2(random.randint(file.get('scale')[0][1], file.get('scale')[1][1]))),
                                      file.get('randomSpread'), file.get('randomVertical'))
        

        DelayEvent(self.main, self.params.lifetime*1000, self.Destroy())
        

    def update(self):
        for i in range(self.params.spawnRate):
            self.spawnParticle()

    def spawnParticle(self):
        self.particles.append(Particle(self.transform, (self.params.velocity), self.params.lifetime, self.params.sprite, self.main.dt))
        