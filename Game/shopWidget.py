from Engine.Widget.button import Button
from Engine.Widget.text import Text
from Engine.Widget.image import Image
from Engine.gameObject import GameObject
from Engine.transform import Transform
from pygame.math import Vector2 as Vec2 
from Engine.Widget.widget import Widget
import pygame
import Engine.serialization as serialize

class ShopButton(Button):
    def __init__(self, main, transform: Transform, owner: "ShopWidget", item: str):
        transform = Transform(transform.pos + Vec2(28, 0), transform.rot, transform.scale)
        super().__init__(main, "shopWidget\\btn_bg.png", transform, 1)
        self.owner = owner
        self.item = item
        self.AddSubscribersForClickEvent(self.click)
        #self.AddSubscribersForHoverEvent(self.hovered)

    def click(self):
        if self.main.player.coins >= self.owner.items[self.item]['cost']:
            self.main.player.coins -= self.owner.items[self.item]['cost']

            self.main.player.attributes[self.item] += self.owner.items[self.item]['adder']
            self.owner.items[self.item]['cost'] = round(self.owner.items[self.item]['cost'] * 1.4)
            
            self.main.player.maxSpeed = self.main.player.attributes['Max Speed']
            self.main.player.acceleration = self.main.player.attributes['Acceleration']
            self.main.player.coinMultiplier = self.main.player.attributes['Coin Multiplier']

            self.main.player.hideShop()

    def hovered(self):
        print("Hovered")

class ShopWidget(Widget):
    def __init__(self, main, transform: Transform):
        super().__init__(main, transform, 0)

        self.children = []
        self.items = {"Max Speed": {"cost": 20, "unit": "km/h", "adder": 0.5}, 
                      "Acceleration": {"cost": 10, "unit": "m/s", "adder": 0.01}, 
                      "Coin Multiplier": {"cost": 100, "unit": "x", "adder": 0.1}}
        
        self.size = self.transform.scale

        self.visible = False
        self.background = Image(self.main, transform, 0, "UI\\shopWidget\\background.png")
        self.add_child(self.background)
        self.playerAttrs = self.main.player.attributes
        self.owner = None
        
    def start(self):
        if serialize.DoesSaveDataExist("shop"):
            self.load()

        text = Text(self.main, "Shop", Transform(self.transform.pos + Vec2(217, 0), 0, Vec2(32,32)), 2)
        self.add_child(text)
        pos = Vec2(220, 100) + self.transform.pos
        for key in self.items:
            self.items[key]['objects'] = {}
            values = self.items[key]
            self.items[key]["objects"]["txt"] = Text(self.main, f"{key}: {round(self.playerAttrs[key], 2)}{values['unit']}", Transform(round(pos), 0, Vec2(32,32)), size=48, zOrder=2)
            
            pos += Vec2(0,90)
            self.items[key]["objects"]["btn"] = ShopButton(self.main, Transform(round(pos/8), 0, Vec2(32,32)), self, key)
            self.items[key]["objects"]["btn_txt"] = Text(self.main, f"Add {values['adder']}{values['unit']} for {values['cost']} coins", Transform(round(pos - Vec2(-20, 10)), 0, Vec2(32,32)), size=32, zOrder=2)

            pos += Vec2(0,100)

            for item in self.items[key]["objects"]:
                self.add_child(self.items[key]["objects"][item])

        for item in self.children:
            item.visible = self.visible

    def add_child(self, child : GameObject):
        self.children.append(self.main.Instantiate(child))

    def update(self):
        if self.playerAttrs != self.main.player.attributes:
            self.playerAttrs = self.main.player.attributes
            for key in self.items:
                values = self.items[key]
                objects = values['objects']

                objects['txt'].text = f"{key}: {round(self.playerAttrs[key], 2)}{values['unit']}"
                objects['btn_txt'].text = f"Add {values['adder']}{values['unit']} for {values['cost']} coins"

        for event in self.main.events:
            if event.type == pygame.QUIT:
                self.save()
        
    
    def save(self):
        data = {}
        for key in self.items:
            values = self.items[key]
            data[key] = {x: values[x] for x in values if x not in {"objects"}}
        
        serialize.SaveData("shop", data)

    def load(self):
        self.items = serialize.LoadSaveData("shop")

    def setVisible(self, visible):
        self.visible = visible
        for child in self.children:
            child.visible = self.visible
        self.main.paused = self.visible