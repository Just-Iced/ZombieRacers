import sys, os
sys.path.append(os.getcwd())

from Engine.main import main
from Engine.transform import Transform
from pygame.math import Vector2
from car import Car
from grass import Grass
from road import Road
from zombie import Zombie
game = main()

#put game logic here:
car = Car(game, Transform(Vector2(90,90), 0, Vector2(16,16)))
grass = Grass(game, Transform(Vector2(90,45), 0, Vector2(16,16)))
zombie = Zombie(game, Transform(Vector2(106,45), 0, Vector2(3,3)))
roads = []
for i in range(10):
    road = Road(game, Transform(Vector2(90,144*i), 0, Vector2(16,16)), -i)
    roads.append(road)

game.run()