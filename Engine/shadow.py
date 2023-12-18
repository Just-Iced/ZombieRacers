import pygame
from Engine.gameObject import GameObject
from json import load
import os

class Shadow:
    def __init__(self, owner: GameObject):
        file = load(open(os.getcwd()+'\\Game\\PreCalculatedObjects.json'))
        voxelPath = file.get(owner.__class__.__name__).get('path')
        findPath = os.getcwd()+'/Game/'+voxelPath+'/'
        sprites = [pygame.image.load(findPath+img).convert_alpha() for img in os.listdir(findPath)]
        self.flatIMG = sprites[0].copy()
        for image in sprites:
            self.flatIMG.blit(image, (0,0))
        self.shadow = pygame.mask.from_surface(self.flatIMG).to_surface(setcolor=(0,0,0,100), unsetcolor=(0,0,0,0))