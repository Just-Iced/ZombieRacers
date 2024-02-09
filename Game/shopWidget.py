from Engine.Widget.button import Button
from Engine.Widget.text import Text
from Engine.Widget.image import Image
from Engine.Widget.widget import Widget
from Engine.transform import Transform
from pygame.math import Vector2 as Vec2 

class ShopWidget(Widget):
    def __init__(self, main, transform: Transform):
        super().__init__(main, transform)
        self.size = self.transform.scale
        self.itemCount = 3
        self.background = self.main.Insantiate(Image(self.main, Transform(Vec2(20,20),0,Vec2(32,32)), "shopWidget\\background.png"))
        self.background.visible = False
        
    def start(self):
        for i in range(self.itemCount):
            ...
