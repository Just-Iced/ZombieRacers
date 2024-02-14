from Engine.main import main
from Engine.gameObject import GameObject
from Engine.transform import Transform
from pygame.math import Vector2 as Vec2
from car import Car
from Engine.Widget.button import Button
from Engine.Widget.text import Text
from Engine.Widget.image import Image
from crate import Crate
from zombieHorde import ZombieHorde
from Engine.Widget.text import Text
import Engine.serialization as serialize
from roadGenerator import RoadGenerator
from shop import Shop
from shopWidget import ShopWidget
import pygame
import importlib
import math
class Game(main):
    def __init__(self, window):
        super().__init__(window)
        self.roadGenerator = None
        self.roadGenerator = self.Instantiate(RoadGenerator(self, Transform(Vec2(90,-85),0,Vec2(1,1)),0))
        self.obj_dict = {}
        self.player = self.Instantiate(Car(self, Transform(Vec2(90,95), 180, Vec2(16,16))))
        if serialize.DoesSaveDataExist("objects"):
            self.obj_dict = serialize.LoadSaveData("objects")
            self.load()
        else:
            horde = self.Instantiate(ZombieHorde(self, Transform(Vec2(90,0), 0, Vec2(85,16))))
            c = self.Instantiate(Crate(self, Transform(Vec2(90,120), 0, Vec2(16,16))))
            s = self.Instantiate(Shop(self, Transform(Vec2(60,120), 180, Vec2(16,16))))

        self.txt = self.Instantiate(Text(self, '', Transform(Vec2(20,20), 0, Vec2(32,16)), zOrder=1))
        self.shopWidget = self.Instantiate(ShopWidget(self, Transform(Vec2(75, 45), 0, Vec2(32,32))))



    def tick(self):
        self.txt.text = f"Coins: {math.floor(self.player.coins)}"
        for event in self.events:
            if event.type == pygame.QUIT:
                self.save()
            
    def load(self):
        for obj in self.obj_dict:
            attrs = self.obj_dict[obj] #attributes
            module = importlib.import_module(attrs["module name"])
            gameObject = self.LoadObject(getattr(module, attrs["class name"])(main = self, transform = attrs["transform"], zOrder=attrs["zOrder"]))
            if isinstance(gameObject, Car):
                self.player = gameObject
            elif isinstance(gameObject, RoadGenerator):
                self.roadGenerator = gameObject
            self.objects.append(gameObject) 

    def save(self):
        self.obj_dict = {}
        for obj in self.objects:
            try:
                if obj.saveable:
                    this_dict = {"module name" : obj.__module__, "class name": obj.__class__.__name__, 
                                                "transform": obj.transform, "zOrder": obj.zOrder}
                    self.obj_dict[str(obj.uid)] = this_dict
            except AttributeError:
                pass
        print(self.obj_dict)
        serialize.SaveData("objects", self.obj_dict)

