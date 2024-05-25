from init import *
from config import *

pygame.font.init()
p = 0.2

class Game:
    """
    Đại diện cho vòng lặp chính và cơ chế của trò chơi Flappy Bird.

    Phương thức
    -----------
    __init__():
        Khởi tạo trò chơi, thiết lập hiển thị và tải các tài nguyên ban đầu.

    draw_all(dt):
        Vẽ tất cả các phần tử trò chơi lên màn hình, cập nhật vị trí của chúng dựa trên delta time.

    check_collision():
        Kiểm tra va chạm giữa chim và ống hoặc đất/trần nhà.
        Trả về False nếu phát hiện va chạm, ngược lại trả về True.

    game_over():
        Hiển thị thông báo game over.

    reset():
        Đặt lại chim và điểm số để bắt đầu trò chơi mới.

    run():
        Chạy vòng lặp chính của trò chơi, xử lý các sự kiện, cập nhật trạng thái trò chơi và hiển thị.
    """
    
    def __init__(self):
        """
        Khởi tạo trò chơi bằng cách thiết lập hiển thị, tải biểu tượng và khởi tạo các thành phần trò chơi.
        """
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        icon = pygame.image.load("assets/birdup.png")
        pygame.display.set_icon(icon)
        self.background = Background()
        self.floor = Floor()
        self.bird = Bird()
        self.score = Score()
        self.pipe = Pipe()
        self.game_over_message = GameOverMessage()

    def draw_all(self, dt):
        """
        Vẽ tất cả các phần tử trò chơi bao gồm nền, sàn, chim, điểm số và các ống.

        Tham số
        -------
        dt : float
            Thời gian delta giữa các khung hình để đảm bảo chuyển động mượt mà.
        """
        self.background.draw()
        self.floor.draw()
        self.bird.draw(dt)
        self.score.draw()
        self.pipe.pipe_list = self.pipe.move()
        self.pipe.draw()

    def check_collision(self):
        """
        Kiểm tra xem chim có va chạm với bất kỳ ống hoặc đất/trần nhà không.

        Trả về
        -------
        bool
            False nếu phát hiện va chạm, ngược lại True.
        """
        if self.bird.image_rect.bottom >= 668 or self.bird.image_rect.top <= -75:
            return False
        for pipe in self.pipe.pipe_list:
            if self.bird.image_rect.colliderect(pipe[0]) or self.bird.image_rect.colliderect(pipe[1]):
                return False
        return True

    def game_over(self):
        """
        Vẽ thông báo game over lên màn hình.
        """
        self.game_over_message.draw(27, 300)

    def reset(self):
        """
        Đặt lại các thành phần trò chơi về trạng thái ban đầu để bắt đầu trò chơi mới.
        """
        self.bird = Bird()
        self.score = Score()
        self.pipe = Pipe()
    def run(self):
        """
        Chạy vòng lặp chính của trò chơi, xử lý nhập liệu của người dùng, cập nhật trạng thái trò chơi, kiểm tra va chạm và hiển thị các khung hình.
        """
        last_time = time.time()
        spawnpipe = pygame.USEREVENT
        pygame.time.set_timer(spawnpipe, 800)
        game_play = True
        while True:
            # Tính toán delta time
            new_time = time.time()
            dt = new_time - last_time
            last_time = new_time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.is_enter_pressed = True
                        self.bird.update_on = True
                    if event.key == pygame.K_SPACE and game_play:
                        self.bird.flap(dt)
                    if event.key == pygame.K_SPACE and  game_play == False:
                        self.reset()
                        game_play = True
                if event.type == spawnpipe:
                    self.pipe.pipe_list.append(self.pipe.create_pipe())
            if game_play:
                self.draw_all(dt)
                self.score.score += 0.01
                if self.score.score > self.score.high_score:
                    self.score.high_score = self.score.score
                game_play = self.check_collision()
            else:
                self.game_over()
            pygame.display.update()

game = Game()
game.run()
