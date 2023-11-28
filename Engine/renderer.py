import pygame

class Renderer:
    def __init__(self, objects, window, camera):
        self.objects = objects
        self.window = window
        self.screen = pygame.Surface((180,90))
        self.cam = camera

    def render(self):
        self.screen.fill((0,0,0))
        self.cam.createTransform()
        self.angle = self.cam.rot
        self.objects.sort(key=lambda x: x.zOrder, reverse=False)
        for object in self.objects:
            tf = self.cam.applyTransform(object.transform.pos)
            for i, img in enumerate(object.sprites):
                rotatedimg = pygame.transform.rotate(img, object.transform.rot - self.angle)
                self.screen.blit(rotatedimg, (tf[0][0] - rotatedimg.get_width() // 2, tf[1][0] - rotatedimg.get_height() // 2 - i * object.spread))
                
        self.display()
                
    def display(self):
        s = pygame.transform.scale(self.screen, (1280, 720))
        
        self.window.window.blit(s, (0,0))