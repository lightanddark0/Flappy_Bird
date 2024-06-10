from init import *
from config import *

class Sprites:
    """
    Đại diện cho các đối tượng có trong trò chơi Flappy Bird.

    Phương thức
    -----------
    __init__(url: str, scale2x: bool):
        Khởi tạo đối tượng sprite, tải hình ảnh từ đường dẫn và tùy chọn phóng to hình ảnh.

    draw(image_x: int, image_y: int):
        Vẽ hình ảnh của sprite lên màn hình tại vị trí xác định.
    """
    
    def __init__(self, url: str, scale2x: bool):
        """
        Khởi tạo đối tượng sprite, tải hình ảnh từ đường dẫn và tùy chọn phóng to hình ảnh.

        Tham số
        -------
        url : str
            Đường dẫn đến hình ảnh của sprite (không bao gồm phần 'assets/' và phần mở rộng '.png').
        scale2x : bool
            Nếu True, phóng to hình ảnh lên gấp đôi.
        """
        self.image = pygame.image.load(f'assets/{url}.png')
        if scale2x:
            self.image = pygame.transform.scale2x(self.image)

    def draw(self, image_x: int, image_y: int):
        """
        Vẽ hình ảnh của sprite lên màn hình tại vị trí xác định.

        Tham số
        -------
        image_x : int
            Vị trí x để vẽ hình ảnh.
        image_y : int
            Vị trí y để vẽ hình ảnh.
        """
        screen.blit(self.image, (image_x, image_y))
