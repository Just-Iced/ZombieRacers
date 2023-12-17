import pygame
from Engine.ParticleSystem.system import System
from Engine.spriteStack import SpriteStack
import math

class Renderer:
    def __init__(self, objects, window, camera):
        self.objects = objects
        self.window = window
        self.screen = pygame.Surface((self.window.window.get_width()/8, self.window.window.get_height()/8))
        self.cam = camera

    def render(self):
        self.screen.fill((0,0,0))
        self.cam.createTransform()
        self.angle = self.cam.rot
        self.objects.sort(key=lambda x: x.zOrder, reverse=False)
        systems = []

        for object in self.objects:
            tf = self.cam.applyTransform(object.transform.pos)
            transform = pygame.math.Vector2(tf[0], tf[1])
            if self.checkShouldRender(transform) == True:
                if isinstance(object, System):
                    systems.append(object)
                
                if isinstance(object, SpriteStack):
                        self.renderShadow(object, transform)
                        
                        rotfrac = (((object.transform.rot + self.cam.rot) + 180 / object.cache) % 360) / 360
                        i = math.floor(rotfrac * object.cache)

                        self.screen.blit(object.rotCache[i][1], transform - object.rotCache[i][0])
        
        self.renderParticles(systems)
        
        self.display()
                
    def display(self):
        s = pygame.transform.scale(self.screen, (self.window.window.get_width(), self.window.window.get_height()))
        self.window.window.blit(s, (0,0))
        pygame.display.update()
    
    def checkShouldRender(self, tf):
        if tf.x > 280 or tf.x < -280 or tf.y > 190 or tf.y < -190:
            return False
        return True
    
    def renderShadow(self, object, transform):
        try:
            shadow = pygame.transform.rotate(object.shadow.shadow, object.transform.rot + self.cam.rot)
            self.screen.blit(shadow, transform - pygame.math.Vector2(shadow.get_width()//2, shadow.get_height()//2))
        except:pass
    
    def renderParticles(self, systems):
        for system in systems:
            for particle in system.particles:
                tf = self.cam.applyTransform(particle.transform.pos)
                transform = pygame.math.Vector2(tf[0], tf[1])
                self.screen.blit(particle.surface, transform)