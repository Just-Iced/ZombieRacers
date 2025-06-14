from Engine.transform import Transform
from pygame.math import Vector2 as Vec2
from Engine.physicsObject import ColliderState
from Engine.spriteStack import SpriteStack
from roadPiece import RoadPiece
from roadDirection import RoadDirection
from shop import Shop
import random

class StraightSide(SpriteStack):
    def __init__(self, main, transform : Transform, zOrder = 20):
        super().__init__(main, transform, zOrder)
        self.physics.simulate = True
        self.physics.scale = 0
        self.physics.colliderState = ColliderState.Block

class RoadStraight(RoadPiece):
    entryDirection = RoadDirection.South
    exitDirecton = RoadDirection.North
    def __init__(self, main, transform: Transform, zOrder=0):
        super().__init__(main, transform, zOrder)
        #TODO: Fix a deleted road having its sides, change the +144 to 0 after
        self.children.append(self.main.Instantiate(StraightSide(self.main, Transform(Vec2(self.transform.pos.x-55, self.transform.pos.y + 144), 0, Vec2(12, 144)))))
        self.children.append(self.main.Instantiate(StraightSide(self.main, Transform(Vec2(self.transform.pos.x+55, self.transform.pos.y + 144), 180, Vec2(12, 144))))) 
        
    def start(self):
        super().start()
        if random.randint(0,10) == 4:
            pos = self.transform.pos + Vec2(random.choice([-30,30]), random.uniform(-65,65))
            self.children.append(self.main.Instantiate(Shop(self.main, Transform(pos, 180, Vec2(16,16)))))
        
    
