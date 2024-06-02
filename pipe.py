from init import *
from config import *

class Pipe(Sprites):
    """
    Đại diện cho đối tượng ống trong trò chơi Flappy Bird.

    Phương thức
    -----------
    __init__():
        Khởi tạo đối tượng ống, tải hình ảnh cho các ống trên và dưới, và khởi tạo danh sách các ống.

    create_pipe():
        Tạo và trả về một cặp ống mới với vị trí ngẫu nhiên.

    move():
        Di chuyển tất cả các ống trong danh sách sang trái và trả về danh sách các ống đã được di chuyển.

    draw():
        Vẽ tất cả các ống lên màn hình.
    """
    
    def __init__(self):
        """
        Khởi tạo đối tượng ống, tải hình ảnh cho các ống trên và dưới, và khởi tạo danh sách các ống.
        """
        pipe_down = Sprites("pipe-green", True)
        self.pipe_down = pipe_down.image
        pipe_up = Sprites("pipe-up", True)
        self.pipe_up = pipe_up.image
        self.pipe_list = []
        self.space_min = 750
        self.speed = 1.6
    def create_pipe(self):
        """
        Tạo và trả về một cặp ống mới với vị trí ngẫu nhiên.

        Trả về
        -------
        list
            Danh sách chứa hai đối tượng hình chữ nhật đại diện cho ống trên và ống dưới.
        """
        self.pipe_high = random.randint(650, 800)
        self.space = random.randint(self.space_min, self.space_min + 100)
        self.pipe_down_rect = self.pipe_up.get_rect(center=(800, self.pipe_high))
        self.pipe_up_rect = self.pipe_down.get_rect(center=(800, self.pipe_high - self.space))
        return [self.pipe_down_rect, self.pipe_up_rect]

    def move(self):
        """
        Di chuyển tất cả các ống trong danh sách sang trái.

        Trả về
        -------
        list
            Danh sách các ống đã được di chuyển.
        """
        for pipe in self.pipe_list:
            pipe[0].centerx -= self.speed
            pipe[1].centerx -= self.speed
        return self.pipe_list
    def check_score(self, score):
        if self.pipe_list != [] and self.pipe_list[score][0].centerx == 0:
            return True
        
    def draw(self):
        """
        Vẽ tất cả các ống lên màn hình.
        """
        for pipe in self.pipe_list:
            screen.blit(self.pipe_down, pipe[0])
            screen.blit(self.pipe_up, pipe[1])
