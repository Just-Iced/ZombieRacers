import pygame
import math
import numpy



class Camera:
    def __init__(self, main):
        self.pos = pygame.math.Vector2(0,0)
        self.offset = pygame.math.Vector2(90,45)
        self.zoom = 1
        self.rot = 0
        
        self.main = main
        
        self.mPos = []
        
        self.mOffset = []
        
        self.mRot = []

        self.mZoom = []
    
    def createTransform(self):
        
        angle = self.rot * math.pi/180
        
        self.mPos = [[1,0,-self.pos.x],
                [0,1,-self.pos.y],
                [0,0,1]]
        
        self.mOffset = [[1,0,self.offset.x],
                   [0,1,self.offset.y],
                   [0,0,1]]
        
        self.mRot = [[math.cos(angle), math.sin(angle), 0],
                [-math.sin(angle), math.cos(angle), 0],
                [0,0,1]]
        
        self.mZoom = [[self.zoom, 0,0],
                 [0,self.zoom,0],
                 [0,0,1]]
    

    def applyTransform(self, vec):
        thing = numpy.dot(self.mPos, [[vec.x],[vec.y],[1]])
        thing2 = numpy.dot(self.mRot, thing)
        thing3 = numpy.dot(self.mZoom, thing2)
        return numpy.around(numpy.dot(self.mOffset, thing3), 1)