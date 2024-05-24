from init import *
from config import *
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