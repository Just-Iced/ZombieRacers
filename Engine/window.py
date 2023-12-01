import pygame

class Window:
    def __init__(self):
        
        pygame.init()
        
        self.flags = (pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.HWACCEL)

        self.window = pygame.display.set_mode((1280, 720), self.flags, vsync=1)

        pygame.display.set_caption("Zombie Racer")