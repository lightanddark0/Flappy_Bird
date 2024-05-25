from init import *
from config import *

class Bird(Sprites):
    """
    Đại diện cho đối tượng chim trong trò chơi Flappy Bird.

    Phương thức
    -----------
    __init__():
        Khởi tạo đối tượng chim, thiết lập vị trí ban đầu và các thuộc tính chuyển động.

    draw(dt):
        Vẽ chim lên màn hình và áp dụng trọng lực để cập nhật vị trí của chim.

    flap(dt):
        Tạo hiệu ứng chim vỗ cánh, thay đổi vận tốc theo hướng lên trên.

    applyGravity(dt):
        Áp dụng trọng lực để thay đổi vận tốc và vị trí của chim.
    """
    
    def __init__(self):
        """
        Khởi tạo đối tượng chim, thiết lập hình ảnh, vị trí ban đầu và các thuộc tính chuyển động.
        """
        Sprites.__init__(self, "midbird", True)
        self.x = 100
        self.image_rect = self.image.get_rect(center=(100, 386))
        
        self.y_velocity = 0
        self.gravity = 10
        self.flap_speed = 650
        self.update_on = False

    def draw(self, dt):
        """
        Vẽ chim lên màn hình và áp dụng trọng lực để cập nhật vị trí của chim.

        Tham số
        -------
        dt : float
            Thời gian delta giữa các khung hình để đảm bảo chuyển động mượt mà.
        """
        self.applyGravity(dt)
        screen.blit(self.image, self.image_rect)

    def flap(self, dt):
        """
        Tạo hiệu ứng chim vỗ cánh, thay đổi vận tốc theo hướng lên trên.

        Tham số
        -------
        dt : float
            Thời gian delta giữa các khung hình để đảm bảo chuyển động mượt mà.
        """
        self.y_velocity = -self.flap_speed * dt

    def applyGravity(self, dt):
        """
        Áp dụng trọng lực để thay đổi vận tốc và vị trí của chim.

        Tham số
        -------
        dt : float
            Thời gian delta giữa các khung hình để đảm bảo chuyển động mượt mà.
        """
        self.y_velocity += self.gravity * dt
        self.image_rect.y += self.y_velocity
