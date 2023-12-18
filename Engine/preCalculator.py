from json import load
import pygame
import os

class PreCalculator:
    def __init__(self):
        file = load(open(os.getcwd()+'\\Game\\PreCalculatedObjects.json'))
        self.objects = {}
        for value in file:
            voxelPath = file.get(value).get('path')
            findPath = os.getcwd()+'/Game/'+voxelPath+'/'
            sprites = [pygame.image.load(findPath+img).convert_alpha() for img in os.listdir(findPath)]     
            
            cache = file.get(value).get('cache')
            rotCache = []
            rotations = []
            
            for rot in range(cache):
                angle = rot / cache * 360
                rotations.append([])
                for image in sprites:
                    rotations[rot].append(pygame.transform.rotate(image, angle))
                    
            if len(sprites) > 1:
                for rot in rotations:
                    maxWidth = max([image.get_width() for image in rot])
                    bottomExtend = rot[0].get_height() // 2
                    topExtend = rot[-1].get_height() // 2
                    renderOffset = (maxWidth / 2, topExtend + 1 * (len(rot)-1))
                    surf = pygame.Surface((maxWidth, renderOffset[1] + bottomExtend))
                    for j, image in enumerate(rot):
                        surf.blit(image, (renderOffset[0] - surf.get_width()/2, (renderOffset[1] - j)-surf.get_height()/2))
                    surf.set_colorkey((0,0,0))
                    renderOffset = surf.get_width()//2, surf.get_height()//2
                    rotCache.append((renderOffset, surf))
            
            self.objects[value] = (rotCache, cache)
            
    
