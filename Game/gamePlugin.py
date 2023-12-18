import sys, os
sys.path.append(os.getcwd())

from Engine.main import main
from Engine.transform import Transform
from pygame.math import Vector2 as Vec2
from car import Car
from road import Road
<<<<<<< HEAD
from zombie import Zombie
from spritetest import SpriteTest
from Engine.ParticleSystem.system import System
=======
from spritetest import SpriteTest
>>>>>>> dev
from Engine.window import Window

game = main(Window((1280, 720)))

#put game logic here:
car = Car(game, Transform(Vec2(90,90), 0, Vec2(16,16)))
road = Road(game, Transform(Vec2(90,144), 0, Vec2(85,16)))
<<<<<<< HEAD
=======
a = SpriteTest(game, Transform(Vec2(90,90), 0, Vec2(16,16)))
>>>>>>> dev

game.run()