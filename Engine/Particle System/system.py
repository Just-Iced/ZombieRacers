import sys, os
sys.path.append(os.getcwd())

from Engine.transform import Transform
from Engine.gameObject import GameObject
from systemstucture import SystemStructure

class System(GameObject):
    def __init__(self, main, path, transform: Transform, zOrder=0):
        super().__init__(main, path, transform, zOrder)

        self.params = SystemStructure()