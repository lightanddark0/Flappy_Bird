from init import *
from config import *
class Bird(Sprites):
    def __init__(self):
        Sprites.__init__(self, "midbird", True)
        self.x = 100
        self.image_rect = self.image.get_rect(center=(100, 386))
        
        self.y_velocity=0
        self.gravity=10
        self.flap_speed= 650
        self.anim_counter=0
        self.update_on = False
    def draw(self, dt):
        self.applyGravity(dt)
        screen.blit(self.image, self.image_rect)
    def flap(self,dt):
        self.y_velocity=-self.flap_speed*dt
    def applyGravity(self, dt):
        self.y_velocity += self.gravity*dt
        self.image_rect.y += self.y_velocity

    def playAnimation(self):
        if self.anim_counter==5:
            self.image=self.img_list[self.image_index]
            if self.image_index==0: self.image_index=1
            else: self.image_index=0
            self.anim_counter=0
        
        self.anim_counter+=1