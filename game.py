from init import *
from config import *

pygame.font.init()
p = 0.2

class Game:
    """
    Đại diện cho vòng lặp chính và cơ chế của trò chơi Flappy Bird.

    Các phương thức:
    ---------------
    __init__():
        Khởi tạo trò chơi, thiết lập hiển thị và tải các tài nguyên ban đầu.

    draw_all():
        Vẽ tất cả các phần tử trò chơi lên màn hình, cập nhật vị trí của chúng.

    check_collision(b):
        Kiểm tra va chạm giữa chim và ống hoặc đất/trần nhà. Trả về False nếu phát hiện va chạm, ngược lại trả về True.

    play_sound(sound):
        Phát âm thanh từ tệp âm thanh.

    play_bg_music():
        Phát nhạc nền cho trò chơi.

    game_starts():
        Hiển thị thông điệp bắt đầu trò chơi.

    game_over():
        Hiển thị thông báo game over lên màn hình.

    reset(avatar_option):
        Đặt lại chim và điểm số để bắt đầu trò chơi mới.

    run():
        Chạy vòng lặp chính của trò chơi, xử lý các sự kiện, cập nhật trạng thái trò chơi và hiển thị các khung hình.
    """
    
    def __init__(self):
        """
        Khởi tạo trò chơi bằng cách thiết lập hiển thị, tải biểu tượng và khởi tạo các thành phần trò chơi.
        """
        pygame.init()
        self.play_bg_music()
        pygame.display.setCaption("Flappy Bird")
        icon = pygame.image.load("assets/birdup.png")
        pygame.display.set_icon(icon)
        self.background = Background()
        self.floor = Floor()
        self.bird = Bird(0, 100)
        self.bird2 = Bird(0, 500)
        self.score = Score()
        self.pipe = Pipe()
        self.game_over_message = GameOverMessage()
        self.game_starts_message = GameStartsMessage()
        self.two_player = False
    
    def draw_all(self):
        """
        Vẽ tất cả các phần tử trò chơi bao gồm nền, sàn, chim, điểm số và các ống.
        """
        self.background.draw()
        self.pipe.pipe_list = self.pipe.move()
        self.pipe.draw()
        self.floor.draw()
        self.bird.draw()
        if self.two_player:
            self.bird2.draw()
        self.score.draw()
    
    def check_collision(self, b):
        """
        Kiểm tra va chạm giữa chim và ống hoặc đất/trần nhà.

        Tham số:
        -------
        b : Bird
            Đối tượng chim cần kiểm tra va chạm.

        Trả về:
        -------
        bool
            False nếu phát hiện va chạm, ngược lại trả về True.
        """
        if b.image_rect.bottom >= 668 or b.image_rect.top <= -75:
            self.play_sound("hit.wav")
            self.play_sound("die.wav")
            return False
        for pipe in self.pipe.pipe_list:
            if b.image_rect.colliderect(pipe[0]) or b.image_rect.colliderect(pipe[1]):
                self.play_sound("hit.wav")
                self.play_sound("die.wav")
                return False
        return True
    
    def play_sound(self, sound):
        """
        Phát âm thanh.

        Tham số:
        -------
        sound : str
            Tên tệp âm thanh cần phát.
        """
        sound = pygame.mixer.Sound(f"sound/{sound}")
        pygame.mixer.Sound.play(sound)
    
    def play_bg_music(self):
        """
        Phát nhạc nền.
        """
        pygame.mixer.music.load("sound/bg_40s.mp3")
        pygame.mixer.music.play(-1)
    
    def game_starts(self):
        """
        Hiển thị thông điệp bắt đầu trò chơi.
        """
        self.game_starts_message.image = Sprites("starts", False).image
        self.game_starts_message.draw(0, 0)
        
        if self.two_player:
            self.game_starts_message.draw2()

    def game_over(self):
        """
        Hiển thị thông báo game over lên màn hình.
        """
        self.background.draw_only()
        self.pipe.draw()
        self.floor.draw_only()

        if self.two_player:
            self.game_over_message.draw2()
        else:
            self.game_over_message.draw_message()
            self.score.draw_score_over()

    def reset(self, avatar_option):
        """
        Đặt lại các thành phần trò chơi về trạng thái ban đầu để bắt đầu trò chơi mới.

        Tham số:
        -------
        avatar_option : int
            Tùy chọn avatar cho chim.
        """
        self.bird = Bird(avatar_option, 100)
        if self.two_player:
            self.bird2 = Bird(avatar_option, 500)
        self.score = Score()
        self.pipe = Pipe()

    def run(self):
        """
        Chạy vòng lặp chính của trò chơi, xử lý nhập liệu của người dùng, cập nhật trạng thái trò chơi, kiểm tra va chạm và hiển thị các khung hình.
        """
        spawnpipe = pygame.USEREVENT
        pygame.time.set_timer(spawnpipe, self.pipe.pipe_timer)
        birdflap = pygame.USEREVENT + 1
        pygame.time.set_timer(birdflap, 200)
        running = True
        stars = False
        game_play = True
        new_score = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and game_play and stars:
                        self.play_sound("wing.wav")
                        self.bird.flap()
                    if self.two_player:
                        if event.key == pygame.K_UP and game_play and stars:
                            self.play_sound("wing.wav")
                            self.bird2.flap()
                    if event.key == pygame.K_RETURN and not game_play:
                        self.reset(self.bird.avatar_option)
                        game_play = True
                        stars = False
                    if event.key == pygame.K_SPACE and not stars:
                        new_score = True
                        self.play_sound("stars.mp3")
                        stars = True
                    if event.key == pygame.K_y and not stars:
                        if not self.two_player:
                            screen = pygame.display.set_mode((864, 768))
                            self.two_player = True
                        else:
                            self.two_player = False
                            screen = pygame.display.set_mode((432, 768))
                            self.game_starts()
                    if event.key == pygame.K_1 and not stars:
                        self.bird.avatar_option = 1
                    if event.key == pygame.K_2 and not stars:
                        self.bird.avatar_option = 2
                    if event.key == pygame.K_3 and not stars:
                        self.bird.avatar_option = 3
                    if event.key == pygame.K_4 and not stars:
                        self.bird.avatar_option = 4
                if event.type == spawnpipe and game_play:
                    self.pipe.pipe_list.append(self.pipe.create_pipe())
                if event.type == birdflap:
                    if self.bird.index < 2:
                        self.bird.index += 1
                    else:
                        self.bird.index = 0
                    if self.bird2.index < 2:
                        self.bird2.index += 1
                    else:
                        self.bird2.index = 0    
                    self.bird.image, self.bird.image_rect = self.bird.animation()
                    self.bird2.image, self.bird2.image_rect = self.bird2.animation()
            if stars and game_play:
                pygame.mixer.music.pause()
                self.draw_all()
                increase = self.pipe.check_score(self.score.score)
                if increase:
                    self.play_sound("point.wav")
                    self.score.score += 1
                    if self.score.score % 5 == 0:
                        self.pipe.speed += 0.005
                        self.pipe.space_min -= 1
                        self.pipe.pipe_timer -= 10
                if self.score.score > self.score.high_score:
                    if new_score:
                        new_score = False 
                        self.play_sound("new_best.mp3")
                    self.score.high_score = self.score.score
                    self.score.write_high_score()
                if not self.check_collision(self.bird):
                    game_play = False
                if self.two_player:
                    if not self.check_collision(self.bird2):
                        game_play = False
            elif stars and not game_play:
                pygame.mixer.music.unpause()
                self.game_over()
            elif not stars and game_play:
                self.game_starts()
                self.reset(self.bird.avatar_option)
            pygame.display.update()

game = Game()
game.run()
