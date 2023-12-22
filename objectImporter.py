import sys
import pygame

def clip(surf, rect):
    if type(rect) == tuple:
        rect = pygame.Rect(*rect)
    surf.set_clip(rect)
    image = surf.subsurface(surf.get_clip()).copy()
    surf.set_clip(None)
    return image

pygame.init()
screen = pygame.display.set_mode((100,100))


path = sys.argv[1]
layers = int(sys.argv[2])
src_img = pygame.image.load(path).convert_alpha()

dimensions = (src_img.get_width(), int(src_img.get_height()/layers))
clip_r = pygame.Rect(0,0, *dimensions)

for i in range(layers):
    img = clip(src_img, clip_r)
    pygame.image.save(img, '/'.join(path.split('/')[:-1]) + f'/img_{(layers - i - 1):02}.png')
    clip_r.y += dimensions[1]
    
pygame.quit()