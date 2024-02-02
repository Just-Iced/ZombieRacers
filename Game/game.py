from Engine.main import main
from Engine.gameObject import GameObject
from Engine.transform import Transform
from pygame.math import Vector2 as Vec2
from car import Car
from road import Road
from Engine.Widget.button import Button
from crate import Crate
from zombieHorde import ZombieHorde
import Engine.serialization as serialize
import pygame
import importlib

class Game(main):
    def __init__(self, window):
        super().__init__(window)
        self.obj_dict = {}
        self.player = self.Instantiate(Car(self, Transform(Vec2(90,95), 180, Vec2(16,16))))
        if serialize.DoesSaveDataExist("objects"):
            self.obj_dict = serialize.LoadSaveData("objects")
            self.load()
            self.loaded = True
        else:
            horde = self.Instantiate(ZombieHorde(self, Transform(Vec2(90,0), 0, Vec2(85,16))))
            road = self.Instantiate(Road(self, Transform(Vec2(90,144), 0, Vec2(85,16))))
            road2 = self.Instantiate(Road(self, Transform(Vec2(90,144 + 72), 0, Vec2(85,16))))
            
            c = self.Instantiate(Crate(self, Transform(Vec2(90,120), 0, Vec2(16,16))))

        b = self.Instantiate(Button(self, 'Button.png', Transform(Vec2(90,45), 0, Vec2(32,16))))

    def tick(self):
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