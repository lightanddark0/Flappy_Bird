from init import *
from config import *

class GameOverMessage(Sprites):
    """
    Đại diện cho thông báo game over trong trò chơi Flappy Bird.

    Phương thức:
    ------------
    __init__():
        Khởi tạo thông báo game over, thiết lập hình ảnh và font chữ.

    draw_message():
        Vẽ thông báo game over lên màn hình và hiển thị hướng dẫn cho người chơi.

    draw2():
        Vẽ thông báo game over lên màn hình cho chế độ 2 người chơi.
    """
    def __init__(self):
        """
        Khởi tạo thông báo game over với hình ảnh và font chữ.
        """
        Sprites.__init__(self, "gameover", True)
        self.font = pygame.font.Font("04B_19.TTF", 30)
    
    def draw_message(self):
        """
        Vẽ thông báo game over lên màn hình và hiển thị hướng dẫn cho người chơi.
        """
        self.draw(27, 200)
        self.text = self.font.render("Press Enter to play again", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(225, 500))
        screen.blit(self.text, self.text_rect)
    
    def draw2(self):
        """
        Vẽ thông báo game over lên màn hình cho chế độ 2 người chơi.
        """
        self.draw(250, 200)
        self.text = self.font.render("Press enter to play again", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(450, 500))
        screen.blit(self.text, self.text_rect)
