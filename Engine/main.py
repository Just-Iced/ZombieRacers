from Engine.renderer import Renderer
from Engine.physics import Physics
from Engine.camera import Camera
from Engine.preCalculator import PreCalculator
from Engine.gameObject import GameObject
import pygame
import time
import sys
import threading

fixedUpdateEvent = pygame.event.Event(357, {})

class main:
    def __init__(self, window):
        self.window = window
        self.preCalc = PreCalculator()
        self.objects = []
        self.colliders = []
        
        self.lastTime = time.time()
        self.dt = 0
        
        self.physics = Physics(self.objects)
        self.cam = Camera(self)
        self.renderer = Renderer(self.objects, self.window, self.cam)
        self.events = pygame.event.get()
        self.player = None
        self.loaded = False
    def run(self):
        run = True
        pygame.time.set_timer(fixedUpdateEvent, 50)
        for object in self.objects:
            object.start()
        while run:
            self.update()
        pygame.time.set_timer(fixedUpdateEvent, 0)
    
    def update(self):
        self.dt = time.time() - self.lastTime
        
        self.dt *= 60
        
        self.lastTime = time.time()
        
        self.events = pygame.event.get()        
        
        for object in self.objects:
            object.tick()
            
        self.tick()

        for event in self.events:
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == fixedUpdateEvent.type:
                f = threading.Thread(target=self.fixedUpdate)
                f.start()
                


            
        
        self.physics.update()
        self.renderer.render()

    def tick(self):
        pass

    def Instantiate(self, obj = GameObject):
        from Engine.spawnMethod import SpawnMethod
        obj.spawnMethod = SpawnMethod.Spawned
        self.objects.append(obj)

    def LoadObject(self, obj = GameObject):
        from Engine.spawnMethod import SpawnMethod
        obj.spawnMethod = SpawnMethod.Loaded
        self.objects.append(obj)

    def fixedUpdate(self):
        for object in self.objects:
            object.fixedUpdate()