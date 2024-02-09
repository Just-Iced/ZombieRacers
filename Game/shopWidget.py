from Engine.Widget.button import Button
from Engine.Widget.text import Text
from Engine.Widget.image import Image
from Engine.Widget.widget import Widget
from Engine.transform import Transform

class ShopWidget(Widget):
    def __init__(self, main, transform: Transform):
        super().__init__(main, transform)
        self.size = self.transform.scale
        self.itemCount = 3
        self.background = Image(self.main)
    def start(self):
        for i in range(self.itemCount):
            ...
