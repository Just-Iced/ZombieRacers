import pygame
from Engine.renderlayer import Layer

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

        layers = []
        
        for object in self.objects:
            tf = self.cam.applyTransform(object.transform.pos)
            if self.checkShouldRender(tf) == True:
                for i, img in enumerate(object.sprites):
                    layers.append(Layer(object, img, i + object.zOrder, i, tf))
                
        
        layers.sort(key=lambda x: x.zOrder, reverse=False)
        
        for layer in layers:
            if not layer.transform[0][0] > 180 or not layer.transform[0][0] < 180 or not layer.transform[1][0] > 90 or not layer.transform[1][0] < 90:
                    rotatedimg = pygame.transform.rotate(layer.surface, layer.object.transform.rot + self.angle)
                    self.screen.blit(rotatedimg, (layer.transform[0][0] - rotatedimg.get_width() // 2, layer.transform[1][0] - rotatedimg.get_height() // 2 - layer.i * layer.object.spread))

                
        self.display()
                
    def display(self):
        s = pygame.transform.scale(self.screen, (1280, 720))
        
        self.window.window.blit(s, (0,0))
        
    def checkShouldRender(self, tf):
        if tf[0][0] > 280 or tf[0][0] < -280 or tf[1][0] > 190 or tf[1][0] < -190:
            return False
        return True
