from Engine.window import Window
from Engine.renderer import Renderer
import pygame
import sys

class main:
    def __init__(self):
        self.window = Window()
        self.objects = []
        self.renderer = Renderer(self.objects, self.window)

    def run(self):
        run = True

        while run:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()

            self.update()

            pygame.display.flip()
    
    def update(self):
        pass