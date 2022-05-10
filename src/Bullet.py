import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, direction, screen):
        super().__init__()
        self.x_pos = xpos
        self.y_pos = ypos
        self.screen = screen
        self.speed = 10
        # self.player = player
        self.direction = direction
        self.image = pygame.image.load('assets/redBulletSmaller.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(self.x_pos, self.y_pos))
 
    def update(self):
        self.rect.y += self.speed*math.sin(math.radians(-self.direction))
        self.rect.x += self.speed*math.cos(math.radians(-self.direction))
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100 or self.rect.x > 1300:
            self.kill()
        if self.rect.y <= -100 or self.rect.y > 900:
            self.kill()
