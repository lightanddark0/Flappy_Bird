from init import *
from config import *
class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.font = pygame.font.Font("04B_19.TTF", 40)
    def update(self):
        pass
    def draw(self):
        self.text_score = self.font.render(f"Score: {int(self.score)}", True, (255, 255, 255))
        self.score_rect = self.text_score.get_rect(center=(300, 20))
        screen.blit(self.text_score, self.score_rect)
    