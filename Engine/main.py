from Engine.window import Window
from Engine.renderer import Renderer
from Engine.physics import Physics
from Engine.camera import Camera
from Engine.preCalculator import PreCalculator
import pygame
import time
import sys

class main:
<<<<<<< Updated upstream
    def __init__(self):
        self.window = Window()
=======
    def __init__(self, window):
        self.window = window
        self.preCalc = PreCalculator()
>>>>>>> Stashed changes
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

            self.update()
            self.physics.update()
            self.renderer.render()

            pygame.display.flip()
    
    def update(self):
        for object in self.objects:
<<<<<<< Updated upstream
            object.tick()
=======
            object.tick()
        
        p = threading.Thread(target=self.physics.update)
        p.start()
        p.join()
        
        self.renderer.render()
>>>>>>> Stashed changes
