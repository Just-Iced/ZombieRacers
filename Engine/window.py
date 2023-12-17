import pygame

class Window:
    def __init__(self, dimensions):
        
        pygame.init()
        
        self.flags = (pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.HWACCEL)

        self.window = pygame.display.set_mode(dimensions, self.flags, vsync=1)

        pygame.display.set_caption("Zombie Racer")