import pygame

class Renderer:
    def __init__(self, objects, window):
        self.objects = objects
        self.window = window

    def render(self):
        for object in self.objects:
            for i, img in enumerate(self.objects.sprites):
                rotatedimg = pygame.transform.rotate(img, object.transform.rot)
                self.window.blit(rotatedimg, (object.transform.pos[0] - rotatedimg.get_width() // 2, object.transform.pos[1] - rotatedimg.get_height() // 2 - i * object.spread))