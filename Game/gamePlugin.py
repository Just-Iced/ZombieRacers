import sys, os
sys.path.append(os.getcwd())

from Engine.main import main

game = main()

game.run()