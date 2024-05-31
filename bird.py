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
        Sprites.__init__(self,"upbird", True)
        self.images = [Sprites("upbird", True).image, Sprites("midbird", True).image, Sprites("downbird", True).image]
        self.index = 1
        self.image = self.images[self.index]
        self.x = 100
        self.image_rect = self.image.get_rect(center=(100, 386))
        
        self.y_velocity = 0
        self.gravity = 10
        self.flap_speed = 650
        self.update_on = False
    def rotated(self):
        new_bird = pygame.transform.rotozoom(self.image, -self.y_velocity*3, 1)
        return new_bird
    
    def draw(self, dt):
        """
        Vẽ chim lên màn hình và áp dụng trọng lực để cập nhật vị trí của chim.

        Tham số
        -------
        dt : float
            Thời gian delta giữa các khung hình để đảm bảo chuyển động mượt mà.
        """
        self.applyGravity(dt)
        
        screen.blit(self.rotated_bird, self.image_rect)
    
    def flap(self, dt):
        """
        Tạo hiệu ứng chim vỗ cánh, thay đổi vận tốc theo hướng lên trên.

        Tham số
        -------
        dt : float
            Thời gian delta giữa các khung hình để đảm bảo chuyển động mượt mà.
        """
        self.y_velocity = -2.7 #self.flap_speed * dt
        
    def applyGravity(self, dt):
        """
        Áp dụng trọng lực để thay đổi vận tốc và vị trí của chim.

        Tham số
        -------
        dt : float
            Thời gian delta giữa các khung hình để đảm bảo chuyển động mượt mà.
        """
        self.y_velocity += 0.05 #self.gravity * dt
        self.rotated_bird = self.rotated()
        self.image_rect.y += self.y_velocity
    def animation(self):
        new_image = self.images[self.index]
        new_image_rect = new_image.get_rect(center = (100, self.image_rect.centery))
        return new_image, new_image_rect