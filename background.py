from init import *
from config import *
class Background(Sprites):
    def __init__(self):
        self.x = 0
        Sprites.__init__(self, "background-night", True)
    def draw(self):
        self.x -= 0.5
        if self.x == -432:
            self.x = 0
        Sprites.draw(self, self.x, 0)
        Sprites.draw(self, self.x + 432, 0)