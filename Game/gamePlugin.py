import sys, os
sys.path.append(os.getcwd())

from Engine.main import main
from Engine.transform import Transform
from pygame.math import Vector2 as Vec2
from car import Car
from road import Road
from Engine.window import Window
from Engine.Widget.button import Button
from crate import Crate
game = main(Window((1280, 720)))

#put game logic here:
game.player = Car(game, Transform(Vec2(90,95), 0, Vec2(16,16)))
road = Road(game, Transform(Vec2(90,144), 0, Vec2(85,16)))
road2 = Road(game, Transform(Vec2(90,144 + 72), 0, Vec2(85,16)))
b = Button(game, 'Button.png', Transform(Vec2(0,0), 0, Vec2(32,16)))
c = Crate(game, Transform(Vec2(90,120), 0, Vec2(16,16)))
game.run()