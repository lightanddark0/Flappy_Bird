from init import *
from config import *

class GameStartsMessage(Sprites):
    """
    Đại diện cho thông báo bắt đầu trò chơi trong Flappy Bird.

    Phương thức:
    ------------
    __init__():
        Khởi tạo thông báo bắt đầu trò chơi, thiết lập hình ảnh và font chữ.

    draw2():
        Vẽ thông báo bắt đầu trò chơi cho chế độ 2 người chơi.
    """
    def __init__(self):
        """
        Khởi tạo thông báo bắt đầu trò chơi với hình ảnh và font chữ.
        """
        Sprites.__init__(self, "starts", False)
        self.font = pygame.font.Font("04B_19.TTF", 30)
    
    def draw2(self):
        """
        Vẽ thông báo bắt đầu trò chơi cho chế độ 2 người chơi.
        """
        self.image = Sprites("bg_2", False).image
        self.draw(0, 0)
