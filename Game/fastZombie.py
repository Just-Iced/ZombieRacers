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
from zombie import Zombie

class FastZombie(Zombie):
    def __init__(self, main, transform: Transform, zOrder=10):
        super().__init__(main, transform, zOrder)
        self.initSpeed = random.uniform(0.85,1.1)
        self.damage = 0.05