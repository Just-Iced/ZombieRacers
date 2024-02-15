from Engine.Widget.button import Button
from Engine.Widget.text import Text
from Engine.Widget.image import Image
from Engine.gameObject import GameObject
from Engine.transform import Transform
from pygame.math import Vector2 as Vec2 
from Engine.Widget.widget import Widget
import sys
import pygame



class ResumeButton(Button):
    def __init__(self, main, transform: Transform):
        super().__init__(main, "btn_bg.png", transform, 9)
        self.AddSubscribersForClickEvent(self.clicked)
    def start(self):
        super().start()
        
    def clicked(self):
        self.main.pauseWidget.setVisible(False)

class ExitButton(Button):
    def __init__(self, main, transform: Transform):
        super().__init__(main, "btn_bg.png", transform, 9)
        self.AddSubscribersForClickEvent(self.clicked)
    def clicked(self):
        self.main.events.append(pygame.event.Event(pygame.QUIT, {}))

class PauseWidget(Widget):
    def __init__(self, main, transform: Transform):
        super().__init__(main, transform, 0)

        self.children = []

        self.visible = False
        self.blurred = Image(self.main, Transform(Vec2(80,45), 0, Vec2(32,32)), 5, sprite=self.blurScreen())
        self.add_child(self.blurred)
        #self.background = Image(self.main, transform, 1, "UI\\pauseWidget\\background.png")
        #self.add_child(self.background)
        self.owner = None
        
    def start(self):
        text = Text(self.main, "PAUSED", Transform(self.transform.pos + Vec2(217, 0), 0, Vec2(32,32)), 7)
        self.add_child(text)

        resumeBtn = ResumeButton(self.main, Transform(self.transform.pos - Vec2(10, 24), 0, Vec2(32,32)))
        resumeTxt = Text(self.main, "Resume", Transform(Vec2(250, 100) + self.transform.pos, 0, Vec2(32,32)), 10)
        self.add_child(resumeTxt)
        self.add_child(resumeBtn)

        exitBtn = ExitButton(self.main, Transform(self.transform.pos - Vec2(10, 5), 0, Vec2(32,32)))
        exitTxt = Text(self.main, "Exit", Transform(Vec2(250, 250) + self.transform.pos, 0, Vec2(32,32)), 10)
        self.add_child(exitBtn)
        self.add_child(exitTxt)



        for item in self.children:
            item.visible = self.visible

    def add_child(self, child : GameObject):
        self.children.append(self.main.Instantiate(child))

    def update(self):
        for event in self.main.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.setVisible(not self.visible)

    def setVisible(self, visible):
        self.visible = visible
        self.main.shopWidget.setVisible(False)
        if self.visible:
            self.blurred.sprite = self.blurScreen()
        for child in self.children:
            child.visible = self.visible
        self.main.paused = self.visible

    def blurScreen(self):
        scrsht = self.main.renderer.screen.copy()
        scrsht = pygame.transform.gaussian_blur(scrsht, 2)
        return scrsht
