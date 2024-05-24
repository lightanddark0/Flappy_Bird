from init import *
from config import *

pygame.font.init()
p = 0.2
class Pipe(Sprites):
    def __init__(self):
        pipe_down = Sprites("pipe-green", True)
        self.pipe_down = pipe_down.image
        pipe_up = Sprites("pipe-up", True)
        self.pipe_up = pipe_up.image
        self.pipe_list = []
        
    def create_pipe(self):
        self.pipe_high = random.randint(650, 800)
        self.space = random.randint(700, 800)
        self.pipe_down_rect = self.pipe_up.get_rect(center=(500, self.pipe_high))
        self.pipe_up_rect = self.pipe_down.get_rect(center=(500, self.pipe_high - self.space))
        return [self.pipe_down_rect, self.pipe_up_rect]
    def move(self):
        for pipe in self.pipe_list:
            pipe[0].centerx -= 2
            pipe[1].centerx -= 2
        return self.pipe_list
    def draw(self):
        for pipe in self.pipe_list:
            screen.blit(self.pipe_down, pipe[0])
            screen.blit(self.pipe_up, pipe[1])
class Game: 
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        icon = pygame.image.load("assets/birdup.png")
        pygame.display.set_icon(icon)
        self.background = Background()
        self.floor = Floor()
        self.bird = Bird()
        self.score = Score()
        self.pipe = Pipe()
    def draw_all(self, dt):
        self.background.draw()
        self.floor.draw()
        self.bird.draw(dt)
        self.score.draw()
        self.pipe.pipe_list = self.pipe.move()
        self.pipe.draw()
    def check_collision(self):
        if self.bird.image_rect.bottom >= 668 or self.bird.image_rect.top <= -75:
            return False
        for pipe in self.pipe.pipe_list:
            if self.bird.image_rect.colliderect(pipe[0]) or self.bird.image_rect.colliderect(pipe[1]):
                return False
        return True
    def game_over(self):
        game_over_message = GameOverMessage()
        game_over_message.draw(27, 300)
    def reset(self):
        self.bird = Bird()
        self.score = Score()

    def run(self):
        last_time=time.time()
        spawnpipe = pygame.USEREVENT
        pygame.time.set_timer(spawnpipe, 800)
        game_play = True
        while True:
            #calculating delta time
            new_time=time.time()
            dt=new_time-last_time
            last_time=new_time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.is_enter_pressed = True
                        self.bird.update_on=True
                    if event.key == pygame.K_SPACE and game_play:
                        self.bird.flap(dt)
                    if event.key == pygame.K_SPACE and game_play == False:
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