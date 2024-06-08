from init import *
from config import *
class GameStartsMessage(Sprites):
    def __init__(self):
        Sprites.__init__(self, "starts", False)
        self.font = pygame.font.Font("04B_19.TTF", 30)
    
    def draw2(self):
        self.image = Sprites("bg_2", False).image
        self.draw(0, 0)