from init import *
from config import *

class Bird(Sprites):
    """
    Đại diện cho đối tượng chim trong trò chơi Flappy Bird.

    Các phương thức:
    ---------------
    __init__(avatar_option, x):
        Khởi tạo đối tượng chim, thiết lập vị trí ban đầu và các thuộc tính chuyển động.

    draw():
        Vẽ chim lên màn hình và áp dụng trọng lực để cập nhật vị trí của chim.

    flap():
        Tạo hiệu ứng chim vỗ cánh, thay đổi vận tốc theo hướng lên trên.

    applyGravity():
        Áp dụng trọng lực để thay đổi vận tốc và vị trí của chim.

    animation():
        Thay đổi hình ảnh của chim để tạo hiệu ứng động.
    """
    
    def __init__(self, avatar_option, x):
        """
        Khởi tạo đối tượng chim.

        Thiết lập hình ảnh, vị trí ban đầu và các thuộc tính chuyển động của chim.

        Tham số:
        -------
        avatar_option : int
            Lựa chọn loại hình ảnh cho chim.
        x : int
            Vị trí x ban đầu của chim.
        """
        Sprites.__init__(self, "upbird", True)
        self.images = [Sprites("upbird", True).image, Sprites("midbird", True).image, Sprites("downbird", True).image]
        self.avatar_option = avatar_option
        if self.avatar_option == 1:
            self.images = [Sprites("birddown", True).image, Sprites("birdup", True).image, Sprites("birddown", True).image]
        elif self.avatar_option == 2:
            self.images = [Sprites("mid_gray_bird", True).image, Sprites("up_gray_bird", True).image, Sprites("down_gray_bird", True).image]
        elif self.avatar_option == 3:
            self.images = [Sprites("uppig", True).image, Sprites("midpig", True).image, Sprites("downpig", True).image]
        elif self.avatar_option == 4:
            self.images = [Sprites("up", True).image, Sprites("mid", True).image, Sprites("down", True).image]
        self.index = 1
        self.image = self.images[self.index]
        self.x = x
        self.image_rect = self.image.get_rect(center=(self.x, 386))
        self.y_velocity = 0
        self.gravity = 10
        self.flap_speed = 650
        self.update_on = False
    
    def rotated(self):
        """
        Tạo và trả về hình ảnh chim đã được xoay theo vận tốc hiện tại.

        Trả về:
        -------
        new_bird : Surface
            Hình ảnh chim đã được xoay.
        """
        new_bird = pygame.transform.rotozoom(self.image, -self.y_velocity * 4, 1)
        return new_bird
    
    def draw(self):
        """
        Vẽ chim lên màn hình và áp dụng trọng lực để cập nhật vị trí của chim.
        """
        self.applyGravity()
        screen.blit(self.rotated_bird, self.image_rect)
    
    def flap(self):
        """
        Tạo hiệu ứng chim vỗ cánh, thay đổi vận tốc theo hướng lên trên.
        """
        self.y_velocity = -2.8
    
    def applyGravity(self):
        """
        Áp dụng trọng lực để thay đổi vận tốc và vị trí của chim.

        Trọng lực sẽ làm tăng vận tốc hướng xuống của chim và cập nhật vị trí theo thời gian.
        """
        self.y_velocity += 0.05
        self.rotated_bird = self.rotated()
        self.image_rect.y += self.y_velocity
    
    def animation(self):
        """
        Thay đổi hình ảnh của chim để tạo hiệu ứng động.

        Trả về:
        -------
        new_image : Surface
            Hình ảnh mới của chim.
        new_image_rect : Rect
            Hình chữ nhật bao quanh hình ảnh mới của chim.
        """
        new_image = self.images[self.index]
        new_image_rect = new_image.get_rect(center=(self.x, self.image_rect.centery))
        return new_image, new_image_rect
