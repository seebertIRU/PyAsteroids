import pygame
import circleshape
from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_SHOT_RADIUS)
     
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y >  SCREEN_HEIGHT:
            self.position.y = 0