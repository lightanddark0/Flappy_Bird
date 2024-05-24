from init import *
from config import *
class Sprites:
    def __init__(self, url: str, scale2x: bool):
        self.image = pygame.image.load(f'assets/{url}.png')
        if scale2x == True:
            self.image = pygame.transform.scale2x(self.image)
    def draw(self, image_x: int, image_y: int):
        screen.blit(self.image, (image_x, image_y))