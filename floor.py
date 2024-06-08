from init import *
from config import *

class Floor(Sprites):
    """
    Đại diện cho sàn trong trò chơi Flappy Bird.

    Phương thức
    -----------
    __init__():
        Khởi tạo đối tượng Floor, thiết lập vị trí ban đầu và gọi hàm khởi tạo của lớp cha.

    draw():
        Vẽ sàn lên màn hình, cập nhật vị trí của sàn để tạo hiệu ứng chuyển động liên tục.
    """

    def __init__(self):
        """
        Khởi tạo đối tượng Floor, thiết lập vị trí x ban đầu và gọi hàm khởi tạo của lớp cha với tham số "floor".
        """
        self.x = 0
        Sprites.__init__(self, "floor", True)

    def draw(self):
        """
        Vẽ sàn lên màn hình, cập nhật vị trí của sàn để tạo hiệu ứng chuyển động liên tục.
        Nếu sàn di chuyển ra khỏi màn hình, đặt lại vị trí để tạo hiệu ứng lặp.
        """
        self.x -= 1
        if self.x == -432:
            self.x = 0
        Sprites.draw(self, self.x, 600)
        Sprites.draw(self, self.x + 432, 600)
        Sprites.draw(self, self.x + 432*2, 600)
    def draw_only(self):
        """
        Vẽ sàn không di chuyển
        """
        Sprites.draw(self, self.x, 600)
        Sprites.draw(self, self.x + 432, 600)
        Sprites.draw(self, self.x + 432*2, 600)