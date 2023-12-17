import pygame
from Engine.renderlayer import Layer
from Engine.ParticleSystem.system import System

class Renderer:
    def __init__(self, objects, window, camera):
        self.objects = objects
        self.window = window
        self.screen = pygame.Surface((180,90))
        self.screen.set_alpha(None)
        self.cam = camera

    def render(self):
        self.screen.fill((0,0,0))
        self.cam.createTransform()

        self.objects.sort(key=lambda x: x.zOrder, reverse=False)
        systems = []

        layers = []
        for object in self.objects:
            if isinstance(object, System):
                systems.append(object)
            tf = self.cam.applyTransform(object.transform.pos)
            transform = pygame.math.Vector2(tf[0], tf[1])
            if self.checkShouldRender(transform) == True and not isinstance(object, System):
                
                self.renderShadow(object, layers, transform)
                for i, img in enumerate(object.sprites):
                    layers.append(Layer(object, img, i+1 + object.zOrder, i, transform))
                
        layers.sort(key=lambda x: x.zOrder, reverse=False)
        
        for layer in layers:
            rotatedimg = pygame.transform.rotate(layer.surface, layer.object.transform.rot + self.cam.rot)
            self.screen.blit(rotatedimg, (layer.transform.x - (rotatedimg.get_width() // 2), layer.transform.y - (rotatedimg.get_height() // 2)- layer.i * layer.object.spread))
        
        self.renderParticles(systems)
        
        self.display()
                
    def display(self):
        s = pygame.transform.scale(self.screen, (1280, 720))
        self.window.window.blit(s, (0,0))
        pygame.display.update()

    def renderParticles(self, systems):
        for system in systems:
            for particle in system.particles:
                tf = self.cam.applyTransform(particle.transform.pos)
                transform = pygame.math.Vector2(tf[0], tf[1])
                self.screen.blit(particle.surface, transform)

        
    def checkShouldRender(self, tf):
        if tf.x > 280 or tf.x < -280 or tf.y > 190 or tf.y < -190:
            return False
        return True
    
    def renderShadow(self, object, layers, transform):
        try:
            layers.append(Layer(object, object.shadow.shadow, object.zOrder, 0, transform))
        except:pass