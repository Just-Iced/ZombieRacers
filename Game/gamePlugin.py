import sys, os
sys.path.append(os.getcwd())

from Engine.main import main
from Engine.transform import Transform
from pygame.math import Vector2
from car import Car
from grass import Grass
from road import Road
game = main()

#put game logic here:
car = Car(game, Transform(Vector2(90,90), 0, Vector2(16,16)))
grass = Road(game, Transform(Vector2(90,45), 0, Vector2(16,16)))

game.run()