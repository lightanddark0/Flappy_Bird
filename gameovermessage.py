from init import *
from config import *
class GameOverMessage(Sprites):
    def __init__(self):
        Sprites.__init__(self, "gameover", True)
        self.font = pygame.font.Font("04B_19.TTF", 30)
    def draw_message(self):
        self.draw(27, 200)
        self.text = self.font.render(f"Press enter to try again", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(225, 500))
        screen.blit(self.text, self.text_rect)
    def draw2(self):
        self.draw(250, 200)
        self.text = self.font.render(f"Press enter to try again", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(450, 500))
        screen.blit(self.text, self.text_rect)