from init import *
from config import *

class Floor(Sprites):
    """
    Đại diện cho sàn trong trò chơi Flappy Bird.

    Các phương thức:
    ---------------
    __init__():
        Khởi tạo đối tượng Floor, thiết lập vị trí ban đầu và gọi hàm khởi tạo của lớp cha.

    draw():
        Vẽ sàn lên màn hình, cập nhật vị trí của sàn để tạo hiệu ứng chuyển động liên tục.
    
    draw_only():
        Vẽ sàn lên màn hình mà không có chuyển động.
    """

    def __init__(self):
        """
        Khởi tạo đối tượng Floor.

        Thiết lập vị trí x ban đầu cho sàn và gọi hàm khởi tạo của lớp cha với tham số "floor".
        """
        self.x = 0
        Sprites.__init__(self, "floor", True)

    def draw(self):
        """
        Vẽ sàn lên màn hình và cập nhật vị trí của sàn để tạo hiệu ứng chuyển động liên tục.
        Khi sàn di chuyển hết màn hình vị trí sẽ được đặt lại
        để tạo hiệu ứng lặp liên tục.
        """
        self.x -= 1
        if self.x == -432:
            self.x = 0
        Sprites.draw(self, self.x, 600)
        Sprites.draw(self, self.x + 432, 600)
        Sprites.draw(self, self.x + 432 * 2, 600)
    
    def draw_only(self):
        """
        Vẽ sàn lên màn hình mà không có chuyển động.
        """
        Sprites.draw(self, self.x, 600)
        Sprites.draw(self, self.x + 432, 600)
        Sprites.draw(self, self.x + 432 * 2, 600)
