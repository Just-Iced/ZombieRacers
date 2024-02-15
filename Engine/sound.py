
import pygame
import math

class Sound(Entity):
    def __init__(self, transform: Transform, attenuation, path):
        super().__init__(x, y, 1, 1, 0, 0, [])
        

        self.channel = pygame.mixer.find_channel(True)

        self.attenuation = attenuation
        self.sound = pygame.mixer.Sound(str(settings.projectPath) + "/" + path)

        self.channel.play(self.sound)
        DelayEvent(self.sound.get_length()*1000, self.destroySound, False)

        if self.attenuation > 0:
            self.sound.set_volume(0.0)
            
        
            

        
    def destroySound(self):
        self.sound.stop()

    def update(self):
        if self.attenuation > 0:
            distance = GetDistanceTo(pygame.math.Vector2(self.x,self.y), pygame.math.Vector2(self.scene.Cam.x, self.scene.Cam.y))
            vol = NormalizeToRange(min = self.attenuation,max = 0,val = distance)
            self.sound.set_volume(vol)