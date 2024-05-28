from init import *
from config import *
class GameOverMessage(Sprites):
    def __init__(self):
        Sprites.__init__(self, "gameover", True)
    def draw_message(self):
        self.draw(27, 200)
        Score.draw_score_over()