from init import *
from config import *
class Floor(Sprites):
    def __init__(self):
        self.x = 0
        Sprites.__init__(self, "floor", True)
    def draw(self):
        self.x -= 1
        if self.x == -432:
            self.x = 0
        Sprites.draw(self, self.x, 600)
        Sprites.draw(self, self.x + 432, 600)