import pygame
from Engine.ParticleSystem.system import System
from Engine.spriteStack import SpriteStack
from Engine.sprite import Sprite
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
        renderObjects = []
        
        for object in self.objects:
            transform = self.cam.applyTransform(object.transform.pos)
            if self.checkShouldRender(transform) == True:
                renderObjects.append((object, transform))
                
        renderObjects.sort(key=lambda x: (x[0].zOrder, x[1].y))
        
        for object in renderObjects:
            if isinstance(object[0], System):
                self.renderParticleSystem(object[0])
            
            elif isinstance(object[0], SpriteStack):
                self.renderSpriteStack(object[0], object[1])
                
            elif isinstance(object[0], Sprite):
                self.renderSprite(object[0], object[1])
        
        self.display()

    def renderSpriteStack(self, object, transform):
        self.renderShadow(object, transform)
        
        rotfrac = (((object.transform.rot + self.cam.rot) + 180 / object.cache) % 360) / 360
        i = math.floor(rotfrac * object.cache)

        self.screen.blit(object.rotCache[i][1], transform - object.rotCache[i][0])
    
    def renderShadow(self, object, transform):
        try:
            shadow = pygame.transform.rotate(object.shadow.shadow, object.transform.rot + self.cam.rot)
            self.screen.blit(shadow, transform - pygame.math.Vector2(shadow.get_width()//2, shadow.get_height()//2))
        except:pass

    def renderSprite(self, object, transform):
        img = pygame.transform.rotate(object.sprite, object.transform.rot + self.cam.rot)
        offset = pygame.math.Vector2(img.get_width()/2, img.get_height()/2)
        self.screen.blit(img, transform - offset)
    
    def renderParticleSystem(self, object):
        for particle in object.particles:
            transform = self.cam.applyTransform(particle.transform.pos)
            self.screen.blit(particle.surface, transform)
                
    def display(self):
        s = pygame.transform.scale(self.screen, (self.window.window.get_width(), self.window.window.get_height()))
        self.window.window.blit(s, (0,0))
        pygame.display.update()
    
    def checkShouldRender(self, tf):
        if tf.x > 280 or tf.x < -280 or tf.y > 190 or tf.y < -190:
            return False
        return True
    
