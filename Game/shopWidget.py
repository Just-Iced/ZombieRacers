from Engine.Widget.button import Button
from Engine.Widget.text import Text
from Engine.Widget.image import Image
from Engine.gameObject import GameObject
from Engine.transform import Transform
from pygame.math import Vector2 as Vec2 

class ShopButton(Button):
    def __init__(self, main, transform: Transform):
        transform = Transform(transform.pos + Vec2(28, 0), transform.rot, transform.scale)
        super().__init__(main, "shopWidget\\btn_bg.png", transform)
        self.AddSubscribersForClickEvent(self.click)
        self.AddSubscribersForHoverEvent(self.hovered)

    def click(self):
        print("Clicked")
    def hovered(self):
        print("Hovered")

class ShopWidget(GameObject):
    def __init__(self, main, transform: Transform, zOrder=10):
        super().__init__(main, transform, zOrder)

        self.children = []
        self.items = {"Max Speed": {"cost": 20, "unit": "km/h", "adder": 1, "objects": []}, 
                      "Acceleration": {"cost": 10, "unit": "m/s", "adder": 0.01, "objects": []}, 
                      "Coin Multiplier": {"cost": 100, "unit": "x", "adder": 0.1, "objects": []}}
        
        self.size = self.transform.scale

        self.visible = True
        self.background = Image(self.main, transform, "UI\\shopWidget\\background.png")
        self.add_child(self.background)
        
    def start(self):
        text = Text(self.main, "Shop", Transform(self.transform.pos + Vec2(217, 0), 0, Vec2(32,32)))
        self.add_child(text)
        pos = Vec2(220, 100) + self.transform.pos
        for key in self.items:
            values = self.items[key]
            txt = Text(self.main, key, Transform(round(pos), 0, Vec2(32,32)), size=48)
            
            pos += Vec2(0,90)
            btn_bg = ShopButton(self.main, Transform(round(pos/8), 0, Vec2(32,32)))
            btn_txt = Text(self.main, f"Add {values['adder']}{values['unit']} for {values['cost']} coins", Transform(round(pos - Vec2(-20, 10)), 0, Vec2(32,32)), size=32)

            pos += Vec2(0,105)

            self.add_child(txt)
            self.add_child(btn_bg)
            self.add_child(btn_txt)
        print(self.children)
        for item in self.children:
            item.visible = self.visible


    def add_child(self, child : GameObject):
        self.children.append(self.main.Instantiate(child))
