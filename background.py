from init import *
from config import *

class Background(Sprites):
    """
    Đại diện cho nền trong trò chơi Flappy Bird.

    Phương thức
    -----------
    __init__():
        Khởi tạo đối tượng nền, thiết lập vị trí ban đầu và tải hình ảnh nền.

    draw():
        Vẽ nền lên màn hình, cập nhật vị trí của nền để tạo hiệu ứng chuyển động liên tục.
    """
    
    def __init__(self):
        """
        Khởi tạo đối tượng nền, thiết lập vị trí x ban đầu và tải hình ảnh nền.
        """
        self.x = 0
        Sprites.__init__(self, "background-night", True)

    def draw(self):
        """
        Vẽ nền lên màn hình, cập nhật vị trí của nền để tạo hiệu ứng chuyển động liên tục.
        Nếu nền di chuyển ra khỏi màn hình, đặt lại vị trí để tạo hiệu ứng lặp.
        """
        self.x -= 0.5
        if self.x == -432:
            self.x = 0
        Sprites.draw(self, self.x, 0)
        Sprites.draw(self, self.x + 432, 0)
        Sprites.draw(self, self.x + 432*2, 0)
    def draw_only(self):
        Sprites.draw(self, self.x, 0)
        Sprites.draw(self, self.x + 432, 0)