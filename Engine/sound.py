from Engine.gameObject import GameObject
from Engine.transform import Transform
from pygame.math import Vector2 as Vec2
import pygame
import os
import math

class Sound(GameObject):
    def __init__(self, main, transform: Transform, attenuation:int, path:str, loop=False, pitch: float = 1):
        super().__init__(main, transform, 0)

        self.channel = pygame.mixer.find_channel(True)

        self.attenuation = attenuation
        self.sound = pygame.mixer.Sound(f"{os.getcwd()}\\Game\\Sounds\\{path}")
        self.loop = loop
        self.channel.play(self.sound)
        self.startTime = pygame.time.get_ticks()
        self.duration = self.sound.get_length()*1000

        if self.attenuation > 0:
            self.sound.set_volume(0.0)

    def update(self):
        if pygame.time.get_ticks() - self.startTime >= self.sound.get_length()*1000 and not self.loop:
            self.Destroy()
        if self.attenuation > 0:
            distance = self.transform.pos.distance_to(self.main.cam.pos)
            vol = (distance - self.attenuation) / -self.attenuation
            self.sound.set_volume(vol)
    def Destroy(self):
        self.sound.stop()
        super().Destroy()
        
