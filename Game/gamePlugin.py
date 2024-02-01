import sys, os
sys.path.append(os.getcwd())

from game import Game
from Engine.window import Window

game = Game(Window((1280, 720)))

#put game logic here:

game.run()