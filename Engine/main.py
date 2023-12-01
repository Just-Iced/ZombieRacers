from Engine.window import Window
from Engine.renderer import Renderer
from Engine.physics import Physics
from Engine.camera import Camera
import pygame
import time
import sys

class main:
    def __init__(self):
        self.window = Window()
        self.objects = []
        self.colliders = []
        
        self.lastTime = time.time()
        self.dt = 0
        
        self.physics = Physics(self.objects)
        self.cam = Camera(self)
        self.renderer = Renderer(self.objects, self.window, self.cam)

    def run(self):
        run = True

        while run:
            self.dt = time.time() - self.lastTime
            
            self.dt *= 60
            
            self.lastTime = time.time()
            
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()

            for object in self.objects:
                object.tick()
                
            self.physics.update()
            self.renderer.render()