import pygame

class Window:
    def __init__(self):
        
        pygame.init()
        
        self.flags = (pygame.DOUBLEBUF)

        self.window = pygame.display.set_mode((1280, 720), self.flags, 16)

        pygame.display.set_caption("Zombie Racer")