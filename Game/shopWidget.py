from Engine.Widget.button import Button
from Engine.Widget.text import Text
from Engine.Widget.image import Image
from Engine.gameObject import GameObject
from Engine.transform import Transform
from pygame.math import Vector2 as Vec2 

class ShopWidget(GameObject):
    def __init__(self, main, transform: Transform):
        super().__init__(main, transform)
        self.children = []
        self.items = {"Max Speed": {"cost": 20, "unit": "km/h", "adder": 1, "objects": []}, 
                      "Acceleration": {"cost": 10, "unit": "m/s", "adder": 0.01, "objects": []}, 
                      "Coin Multiplier": {"cost": 100, "unit": "x", "adder": 0.1, "objects": []}}
        
        self.size = self.transform.scale

        self.visible = True
        self.background = Image(self.main, Transform(Vec2(20,20),0,Vec2(32,32)), "UI\\shopWidget\\background.png")
        self.add_child(self.background)
        
    def start(self):
        self.children.append(self.main.Instantiate(Text(self.main, "Shop", Transform(self.transform.pos + Vec2(217, 0), 0, Vec2(32,32)))))
        pos = Vec2(10, 30) + self.transform.pos
        for key in self.items:
            values = self.items[key]
            txt = Text(self.main, key, Transform(pos, 0, Vec2(32,32)))
            
            pos += Vec2(0,20)
            btn_bg = Button(self.main, "shopWidget\\btn_bg.png", Transform(pos, 0, Vec2(32,32)))
            btn_txt = Text(self.main, f"Add {values['adder']} {values['unit']} for {values['cost']} coins", Transform(pos, 0, Vec2(32,32)))

            pos += Vec2(0,20)

            self.add_child(txt)
            self.add_child(btn_bg)
            self.add_child(btn_txt)
        print(self.children)
        for item in self.children:
            item.visible = self.visible

    def add_child(self, child):
        self.children.append(self.main.Instantiate(child))
