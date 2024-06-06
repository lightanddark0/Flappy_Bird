from init import *
from config import *
class GameStarsMessage(Sprites):
    def __init__(self):
        Sprites.__init__(self, "stars", False)
        self.font = pygame.font.Font("04B_19.TTF", 30)
    
    def draw2(self):
        self.image = Sprites("bg_2", False).image
        self.draw(0, 0)