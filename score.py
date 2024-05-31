from init import *
from config import *

class Score:
    """
    Đại diện cho điểm số trong trò chơi Flappy Bird.

    Phương thức
    -----------
    __init__():
        Khởi tạo đối tượng điểm số, thiết lập điểm số ban đầu, điểm cao nhất và phông chữ.

    update():
        Cập nhật điểm số (hiện tại chưa thực hiện chức năng cụ thể).

    draw():
        Vẽ điểm số hiện tại lên màn hình.
    """
    
    def __init__(self):
        """
        Khởi tạo đối tượng điểm số, thiết lập điểm số ban đầu, điểm cao nhất và phông chữ.
        """
        self.score = 0
        self.high_score = 0
        self.font = pygame.font.Font("04B_19.TTF", 40)

    def update(self):
        """
        Cập nhật điểm số (hiện tại chưa thực hiện chức năng cụ thể).
        """
        pass
    def read_high_score(self):
        self.hs_file = open("highscore.txt", "r+")
        res = self.hs_file.readlines(-1)
        if res != None:
            self.high_score = int(res[-1])
    def write_high_score(self):
        self.hs_file.writelines("\n" + str(self.high_score))

    def draw(self):
        """
        Vẽ điểm số hiện tại và điểm cao nhất lên màn hình.
        """
        self.text_score = self.font.render(f"Score: {int(self.score)}", True, (255, 255, 255))
        self.score_rect = self.text_score.get_rect(center=(300, 20))
        screen.blit(self.text_score, self.score_rect)
        self.read_high_score()
        self.text_high_score = self.font.render(f"Best: {int(self.high_score)}", True, (255, 255, 255))
        self.high_score_rect = self.text_high_score.get_rect(center=(300, 60))
        screen.blit(self.text_high_score, self.high_score_rect)
    def draw_score_over(self):
        self.text_score = self.font.render(f"Score: {int(self.score)}", True, (255, 255, 255))
        self.score_rect = self.text_score.get_rect(center=(200, 400))
        screen.blit(self.text_score, self.score_rect)
        self.text_high_score = self.font.render(f"Best: {int(self.high_score)}", True, (255, 255, 255))
        self.high_score_rect = self.text_high_score.get_rect(center=(200, 440))
        screen.blit(self.text_high_score, self.high_score_rect)